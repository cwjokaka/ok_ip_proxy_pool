import asyncio
from typing import List

import aiohttp

from setting import HEADERS
from src.entity.proxy_entity import ProxyEntity
from src.enum.common import ProxyCoverEnum, ProxyTypeEnum
from src.spider.abs_spider import AbsSpider
from bs4 import BeautifulSoup, Tag


spider_collection = {}


def spider_register(cls):
    spider_collection.update({cls.__name__: cls()})
    print(f'注册{cls.__name__}')
    return cls


@spider_register
class Spider66Ip(AbsSpider):
    """
    66IP代理爬虫 刷新速度:🐌慢
    http://www.66ip.cn/
    """
    def __init__(self) -> None:
        super().__init__('66IP代理爬虫')
        self._base_url = 'http://www.66ip.cn'

    async def do_crawl(self) -> List[ProxyEntity]:
        result = []
        for page in range(1, 6):
            # print(f'第{page}页...')
            async with aiohttp.ClientSession() as session:
                async with session.get(f'{self._base_url}/{page}.html') as resp:
                    resp.encoding = 'gb2312'
                    soup = BeautifulSoup(await resp.text(), 'lxml')
                    tr_list = soup.find('table', attrs={'width': '100%', 'bordercolor': '#6699ff'}).find_all('tr')
                    for i, tr in enumerate(tr_list):
                        if i == 0:
                            continue
                        contents = tr.contents
                        ip = contents[0].text
                        port = contents[1].text
                        region = contents[2].text
                        proxy_cover = contents[3].text
                        result.append(ProxyEntity(f'http://{ip}:{port}',
                                                  # ip, port,
                                                  source=self._name,
                                                  proxy_cover=self._judge_proxy_cover(proxy_cover),
                                                  region=region))
        return result

    @staticmethod
    def _judge_proxy_cover(cover_str: str):
        if cover_str == '高匿代理':
            return ProxyCoverEnum.HIGH_COVER.value
        else:
            return ProxyCoverEnum.UNKNOWN.value


@spider_register
class SpiderQuanWangIp(AbsSpider):
    """
    全网IP代理爬虫 刷新速度:极快
    http://www.goubanjia.com/
    """
    def __init__(self) -> None:
        super().__init__('全网IP代理爬虫')
        self._base_url = 'http://www.goubanjia.com'

    async def do_crawl(self) -> List[ProxyEntity]:
        result = []
        async with aiohttp.ClientSession() as session:
            async with session.get(self._base_url, headers=HEADERS) as resp:
                soup = BeautifulSoup(await resp.text(), 'lxml')
                tr_list = soup.find('tbody').find_all('tr')
                for i, tr in enumerate(tr_list):
                    tds = tr.find_all('td')
                    id_and_port = tds[0]
                    ip, port = self._parse_ip_and_port(id_and_port)
                    proxy_cover = tds[1].text
                    proxy_type = tds[2].text
                    region = tds[3].contents[1].text
                    supplier = tds[4].text
                    result.append(ProxyEntity(f'{proxy_type.lower()}://{ip}:{port}',
                                              # ip, port,
                                              # protocol=proxy_type,
                                              source=self._name,
                                              supplier=supplier,
                                              proxy_type=self._judge_proxy_type(proxy_type),
                                              proxy_cover=self._judge_proxy_cover(proxy_cover),
                                              region=region
                                              )
                                  )
        return result


    def _parse_ip_and_port(self, ip_td: Tag):

        res = []
        contents = ip_td.find_all(['div', 'span'])
        for content in contents:
            res.append(content.text)
        res.pop()
        ip = ''.join(res)

        port_tag = contents[-1]
        port_ori_str = port_tag.get('class')[1]
        # 解码真实的端口
        port = 0
        for c in port_ori_str:
            port *= 10
            port += (ord(c) - ord('A'))
        port /= 8
        port = int(port)
        # print(f'ip:{ip}, port:{port}')
        return ip, str(port)

    def _judge_proxy_type(self, type_str: str):
        type_low = type_str.lower()
        if type_low == 'http':
            return ProxyTypeEnum.HTTP.value
        elif type_low == 'https':
            return ProxyTypeEnum.HTTPS.value
        else:
            return ProxyTypeEnum.UNKNOWN.value

    def _judge_proxy_cover(self, cover_str: str):
        if cover_str == '透明':
            return ProxyCoverEnum.TRANSPARENT.value
        elif cover_str == '高匿':
            return ProxyCoverEnum.HIGH_COVER.value
        else:
            return ProxyCoverEnum.UNKNOWN.value


@spider_register
class SpiderXiciIp(AbsSpider):
    """
    西刺代理爬虫 刷新速度:🐌慢
    https://www.xicidaili.com/
    """
    def __init__(self) -> None:
        super().__init__('西刺IP代理爬虫')
        self._base_urls = [
            'https://www.xicidaili.com/nn',     # 高匿
            'https://www.xicidaili.com/nt'      # 透明
            ]

    async def do_crawl(self) -> List[ProxyEntity]:
        result = []
        for base_url in self._base_urls:
            for page in range(1, 3):
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'{base_url}/{page}', headers=HEADERS) as resp:
                        soup = BeautifulSoup(await resp.text(), 'lxml')
                        tab = soup.find('table', attrs={'id': 'ip_list'})
                        if tab is None:
                            continue
                        tr_list = tab.find_all('tr')[1: -1]
                        for tr in tr_list:
                            tds = tr.find_all('td')
                            # country = tds[0].find('img')['alt']
                            ip = tds[1].text
                            port = tds[2].text
                            # city = tds[3].text.replace('\n', '')
                            proxy_cover = tds[4].text
                            proxy_type = tds[5].text
                            result.append(ProxyEntity(f'{proxy_type.lower()}://{ip}:{port}',
                                                      # ip, port,
                                                      # protocol=proxy_type.lower(),
                                                      source=self._name,
                                                      proxy_cover=self._judge_proxy_cover(proxy_cover),
                                                      proxy_type=self._judge_proxy_type(proxy_type),
                                                      ))
                return result

    @staticmethod
    def _judge_proxy_cover(cover_str: str):
        if cover_str == '高匿':
            return ProxyCoverEnum.HIGH_COVER.value
        if cover_str == '透明':
            return ProxyCoverEnum.TRANSPARENT.value
        else:
            return ProxyCoverEnum.UNKNOWN.value

    @staticmethod
    def _judge_proxy_type(type_str: str):
        if type_str == 'HTTPS':
            return ProxyTypeEnum.HTTPS.value
        if type_str == 'HTTP':
            return ProxyTypeEnum.HTTP.value
        else:
            return ProxyTypeEnum.UNKNOWN.value


@spider_register
class SpiderKuaiDaiLiIp(AbsSpider):
    """
    快代理IP 刷新速度: 极快
    https://www.kuaidaili.com/free
    """
    def __init__(self) -> None:
        super().__init__('快代理IP代理爬虫')
        self._base_urls = [
            'https://www.kuaidaili.com/free/inha',     # 高匿
            'https://www.kuaidaili.com/free/intr'      # 透明
            ]

    async def do_crawl(self) -> List[ProxyEntity]:
        result = []
        for base_url in self._base_urls:
            for page in range(1, 3):
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'{base_url}/{page}', headers=HEADERS) as resp:

                        # res = requests.get(f'{base_url}/{page}', headers=HEADERS)
                        soup = BeautifulSoup(await resp.text(), 'lxml')
                        trs = soup.find('table').find('tbody').find_all('tr')
                        for tr in trs:
                            tds = tr.find_all('td')
                            ip = tds[0].text
                            port = tds[1].text
                            proxy_cover = tds[2].text
                            proxy_type = tds[3].text
                            region = tds[4].text
                            result.append(ProxyEntity(f'{proxy_type.lower()}://{ip}:{port}',
                                                      # ip, port, protocol=proxy_type.lower(),
                                                      source=self._name,
                                                      proxy_type=self._judge_proxy_type(proxy_type),
                                                      proxy_cover=self._judge_proxy_cover(proxy_cover),
                                                      region=region))
                # 爬太快会被封
                await asyncio.sleep(3)
        return result

    def _judge_proxy_type(self, type_str: str):
        type_low = type_str.lower()
        if type_low == 'http':
            return ProxyTypeEnum.HTTP.value
        elif type_low == 'https':
            return ProxyTypeEnum.HTTPS.value
        else:
            return ProxyTypeEnum.UNKNOWN.value

    def _judge_proxy_cover(self, cover_str: str):
        if cover_str == '透明':
            return ProxyCoverEnum.TRANSPARENT.value
        elif cover_str == '高匿名':
            return ProxyCoverEnum.HIGH_COVER.value
        else:
            return ProxyCoverEnum.UNKNOWN.value


@spider_register
class SpiderYunDaiLiIp(AbsSpider):
    """
    云代理IP 刷新速度: 快
    http://www.ip3366.net/free
    """
    def __init__(self) -> None:
        super().__init__('云代理IP爬虫')
        self._base_urls = [
            'http://www.ip3366.net/free/?stype=1',     # 高匿
            'http://www.ip3366.net/free/?stype=2'      # 透明 or 普匿
            ]

    async def do_crawl(self) -> List[ProxyEntity]:
        result = []
        for base_url in self._base_urls:
            for page in range(1, 3):
                async with aiohttp.ClientSession() as session:
                    async with session.get(f'{base_url}&page={page}', headers=HEADERS) as resp:

                        # res = requests.get(f'{base_url}/{page}', headers=HEADERS)
                        soup = BeautifulSoup(await resp.text(), 'lxml')
                        trs = soup.find('table').find('tbody').find_all('tr')
                        for tr in trs:
                            tds = tr.find_all('td')
                            ip = tds[0].text
                            port = tds[1].text
                            proxy_cover = tds[2].text
                            proxy_type = tds[3].text
                            region = tds[4].text
                            result.append(ProxyEntity(f'{proxy_type.lower()}://{ip}:{port}',
                                                      # ip, port, protocol=proxy_type.lower(),
                                                      source=self._name,
                                                      proxy_type=self._judge_proxy_type(proxy_type),
                                                      proxy_cover=self._judge_proxy_cover(proxy_cover),
                                                      region=region))
        return result

    def _judge_proxy_type(self, type_str: str):
        type_low = type_str.lower()
        if type_low == 'http':
            return ProxyTypeEnum.HTTP.value
        elif type_low == 'https':
            return ProxyTypeEnum.HTTPS.value
        else:
            return ProxyTypeEnum.UNKNOWN.value

    def _judge_proxy_cover(self, cover_str: str):
        if cover_str == '透明代理IP':
            return ProxyCoverEnum.TRANSPARENT.value
        elif cover_str == '高匿代理IP':
            return ProxyCoverEnum.HIGH_COVER.value
        elif cover_str == '普通代理IP':
            return ProxyCoverEnum.NORMAL_COVER.value
        else:
            return ProxyCoverEnum.UNKNOWN.value


@spider_register
class SpiderIpHaiIp(AbsSpider):
    """
    IP海代理IP 刷新速度: 8分钟/1个
    有时会连不上
    http://www.iphai.com
    """
    def __init__(self) -> None:
        super().__init__('IP海代理IP爬虫')
        self._base_urls = [
            'http://www.iphai.com/free/ng',         # 国内高匿
            'http://www.iphai.com/free/np',         # 国内普通
            'http://www.iphai.com/free/wg',         # 国外高匿
            'http://www.iphai.com/free/wp',         # 国外普通
            ]

    async def do_crawl(self) -> List[ProxyEntity]:
        result = []
        for base_url in self._base_urls:
            async with aiohttp.ClientSession() as session:
                async with session.get(base_url, headers=HEADERS) as resp:
                    soup = BeautifulSoup(await resp.text(), 'lxml')
                    table = soup.find('table')
                    if table is None:
                        continue
                    tbody = soup.find('tbody')
                    if tbody is None:
                        continue
                    trs = tbody.find_all('tr')
                    for i, tr in enumerate(trs):
                        if i == 0:
                            continue
                        tds = tr.find_all('td')
                        ip = tds[0].text
                        port = tds[1].text
                        proxy_cover = tds[2].text
                        proxy_type = tds[3].text if tds[3].text != '' else 'http'
                        region = tds[4].text
                        result.append(ProxyEntity(f'{proxy_type.lower()}://{ip}:{port}',
                                                  # ip, port, protocol=proxy_type.lower(),
                                                  source=self._name,
                                                  proxy_type=self._judge_proxy_type(proxy_type),
                                                  proxy_cover=self._judge_proxy_cover(proxy_cover),
                                                  region=region))
            await asyncio.sleep(2)
        return result

    @staticmethod
    def _judge_proxy_type(type_str: str):
        type_low = type_str.lower()
        if type_low == 'http':
            return ProxyTypeEnum.HTTP.value
        elif type_low == 'https':
            return ProxyTypeEnum.HTTPS.value
        else:
            return ProxyTypeEnum.UNKNOWN.value

    @staticmethod
    def _judge_proxy_cover(cover_str: str):
        if cover_str == '透明':
            return ProxyCoverEnum.TRANSPARENT.value
        elif cover_str == '高匿':
            return ProxyCoverEnum.HIGH_COVER.value
        elif cover_str == '普匿':
            return ProxyCoverEnum.NORMAL_COVER.value
        else:
            return ProxyCoverEnum.UNKNOWN.value


@spider_register
class SpiderMianFeiDaiLiIp(AbsSpider):
    """
    免费代理IP库
    http://ip.jiangxianli.com/
    """
    def __init__(self) -> None:
        super().__init__('免费代理IP爬虫')
        self._base_url = 'http://ip.jiangxianli.com/?page={}'

    async def do_crawl(self) -> List[ProxyEntity]:
        result = []
        for page in range(1, 4):
            async with aiohttp.ClientSession() as session:
                async with session.get(self._base_url.format(page), headers=HEADERS) as resp:
                    soup = BeautifulSoup(await resp.text(), 'lxml')
                    table = soup.find('table')
                    if table is None:
                        continue
                    tbody = soup.find('tbody')
                    if tbody is None:
                        continue
                    trs = tbody.find_all('tr')
                    for i, tr in enumerate(trs):
                        if i == 0:
                            continue
                        tds = tr.find_all('td')
                        ip = tds[1].text
                        port = tds[2].text
                        proxy_cover = tds[3].text
                        proxy_type = tds[4].text if tds[3].text != '' else 'http'
                        region = tds[5].text
                        supplier = tds[6].text
                        result.append(ProxyEntity(f'{proxy_type.lower()}://{ip}:{port}',
                                                  # ip, port, protocol=proxy_type.lower(),
                                                  source=self._name,
                                                  supplier=supplier,
                                                  proxy_type=self._judge_proxy_type(proxy_type),
                                                  proxy_cover=self._judge_proxy_cover(proxy_cover),
                                                  region=region))
            await asyncio.sleep(2)
        return result

    @staticmethod
    def _judge_proxy_type(type_str: str):
        type_low = type_str.lower()
        if type_low == 'http':
            return ProxyTypeEnum.HTTP.value
        elif type_low == 'https':
            return ProxyTypeEnum.HTTPS.value
        else:
            return ProxyTypeEnum.UNKNOWN.value

    @staticmethod
    def _judge_proxy_cover(cover_str: str):
        if cover_str == '透明':
            return ProxyCoverEnum.TRANSPARENT.value
        elif cover_str == '高匿':
            return ProxyCoverEnum.HIGH_COVER.value
        elif cover_str == '普匿':
            return ProxyCoverEnum.NORMAL_COVER.value
        else:
            return ProxyCoverEnum.UNKNOWN.value
