import asyncio
import aiohttp

from setting import VALIDATOR
from src.database.sqlite_opt import sqlite_opt


class Validator(object):

    def run(self):
        # 获取proxy列表
        proxy_list = sqlite_opt.get_all_proxies()
        if len(proxy_list) > 0:
            tasks = [self.valid_proxy(proxy.url) for proxy in proxy_list]
            asyncio.run(asyncio.wait(tasks))

    async def valid_proxy(self, proxy_url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(VALIDATOR['test_url'], proxy=proxy_url,
                                       timeout=VALIDATOR['request_timeout']) as resp:
                    if resp.status == 200:
                        # print(f'{proxy_url}可靠')
                        sqlite_opt.increase_reliability(proxy_url)
                    else:
                        # print(f'{proxy_url}不可靠')
                        sqlite_opt.reduce_reliability(proxy_url)
            except:
                sqlite_opt.reduce_reliability(proxy_url)
                # print(f'{proxy_url}不可靠')


validator = Validator()
