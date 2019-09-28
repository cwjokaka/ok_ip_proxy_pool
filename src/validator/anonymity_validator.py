import asyncio
import json

import aiohttp

from setting import ANONYMITY_VALIDATOR, HEADERS
from src.database.sqlite_opt import sqlite_opt
from src.enum.common import ProxyCoverEnum, ProxyTypeEnum
from src.log.logger import logger


class AnonymityValidator(object):

    urls = {
        ProxyTypeEnum.UNKNOWN.value: ANONYMITY_VALIDATOR['http_test_url'],
        ProxyTypeEnum.HTTP.value: ANONYMITY_VALIDATOR['http_test_url'],
        ProxyTypeEnum.HTTPS.value: ANONYMITY_VALIDATOR['https_test_url'],
        ProxyTypeEnum.HTTP_AND_HTTPS.value: ANONYMITY_VALIDATOR['https_test_url'],
    }

    def run(self):
        # 获取proxy列表
        proxy_list = sqlite_opt.get_unknown_anonymity_proxies()
        if len(proxy_list) > 0:
            tasks = [self.valid_proxy(proxy.url, proxy.proxy_type) for proxy in proxy_list]
            asyncio.run(asyncio.wait(tasks))

    async def valid_proxy(self, proxy_url, proxy_type):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.urls[proxy_type],
                                       proxy=proxy_url,
                                       headers=HEADERS,
                                       timeout=ANONYMITY_VALIDATOR['request_timeout']) as resp:
                    if resp.status == 200:
                        # 检验其匿名性
                        r_dict = json.loads(await resp.text())
                        headers = r_dict.get('headers', '')
                        ip = r_dict.get('origin')
                        proxy_connection = headers.get('Proxy-Connection', None)
                        flag = True
                        if ',' in ip:
                            ips = str.split(ip, ',')
                            first = ips[0]
                            for p in ips:
                                if first != p.lstrip():
                                    proxy_cover = ProxyCoverEnum.TRANSPARENT.value   # 透明
                                    flag = False
                                    break
                        if flag:
                            if proxy_connection:
                                proxy_cover = ProxyCoverEnum.NORMAL_COVER.value  # 普匿
                            else:
                                proxy_cover = ProxyCoverEnum.HIGH_COVER.value    # 高匿
                        # 更新匿名性
                        sqlite_opt.update_anonymity(proxy_url, proxy_cover)
                        logger.info(f'验证匿名性成功: url:{proxy_url}, coverValue:{proxy_cover}')
                    else:
                        logger.warn(f'验证匿名性失败, proxy_url:{proxy_url}, 返回码:{resp.status}')
            except asyncio.TimeoutError:
                logger.warn(f'验证匿名性请求超时, proxy_url:{proxy_url}')
            except ConnectionRefusedError:
                logger.warn(f'验证匿名性请求被拒绝, proxy_url:{proxy_url}')
            except Exception as e:
                # logger.exception(e)
                logger.warn(f'验证匿名性失败, proxy_url:{proxy_url}, e:{e}')


anonymity_validator = AnonymityValidator()
