import asyncio
from asyncio import AbstractEventLoop
from collections import Coroutine
from typing import List, Iterable

import aiohttp
# import requests
from aiohttp import ClientSession

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
        self._base_url = 'http://www.66ip.cn/{}'

    def do_crawl(self, event_loop: AbstractEventLoop) -> Iterable[ProxyEntity]:
        tasks = []
        for page in range(1, 5):
            url = self._base_url.format(page)
            task = asyncio.ensure_future(self._request(url))
            tasks.append(task)
        # for page in range(1, 5):
        #     task = asyncio.ensure_future(hello(self._base_url.format(page)))

        event_loop.call_soon_threadsafe(tasks)

        # for page in range(1, 5):
        #     # print(f'第{page}页...')
        #     # resp = requests.get(f'{self._base_url}/{page}.html')
        #     async with aiohttp.ClientSession() as session:
        #         async with session.get(f'{self._base_url}/{page}.html') as resp:
        #             # await aiohttp
        #             resp.encoding = 'gb2312'
        #             soup = BeautifulSoup(await resp.text(), 'lxml')
        #             tr_list = soup.find('table', attrs={'width': '100%', 'bordercolor': '#6699ff'}).find_all('tr')
        #             for i, tr in enumerate(tr_list):
        #                 if i == 0:
        #                     continue
        #                 contents = tr.contents
        #                 ip = contents[0].text
        #                 port = contents[1].text
        #                 region = contents[2].text
        #                 proxy_cover = contents[3].text
        #                 # check_time = contents[4].text
        #                 # print(f'{ip}:{port}/{region}/{proxy_type}/{check_time}')
        #                 yield ProxyEntity(ip, port,
        #                                   source=self._name,
        #                                   proxy_cover=self._judge_proxy_cover(proxy_cover),
        #                                   region=region)


    async def _request(self, url):
        async with ClientSession() as session:
            async with session.get(url) as response:
                response = await response.read()
                print(response)


    def _judge_proxy_cover(self, cover_str: str):
        if cover_str == '高匿代理':
            return ProxyCoverEnum.HIGH_COVER
        else:
            return ProxyCoverEnum.UNKNOWN


# @spider_register
# class SpiderQuanWangIp(AbsSpider):
#     """
#     全网IP代理爬虫 刷新速度:极快
#     http://www.goubanjia.com/
#     """
#     def __init__(self) -> None:
#         super().__init__('全网IP代理爬虫')
#         self._base_url = 'http://www.goubanjia.com'
#
#     async def do_crawl(self) -> Iterable[ProxyEntity]:
#         resp = requests.get(self._base_url, headers=HEADERS)
#         soup = BeautifulSoup(resp.text, 'lxml')
#         # print(soup.prettify())
#         tr_list = soup.find('tbody').find_all('tr')
#         for i, tr in enumerate(tr_list):
#             tds = tr.find_all('td')
#             id_and_port = tds[0]
#             ip, port = self._parse_ip_and_port(id_and_port)
#             proxy_cover = tds[1].text
#             proxy_type = tds[2].text
#             region = tds[3].contents[1].text
#             supplier= tds[4].text
#             # resp_speed = tds[5].text[:-2]
#             # last_check_time = tds[6]
#             # ttl = tds[7]
#             yield ProxyEntity(ip, port,
#                               source=self._name,
#                               supplier=supplier,
#                               proxy_type=self._judge_proxy_type(proxy_type),
#                               proxy_cover=self._judge_proxy_cover(proxy_cover),
#                               region=region
#                               )
#
#
#     def _parse_ip_and_port(self, ip_td: Tag):
#
#         res = []
#         contents = ip_td.find_all(['div', 'span'])
#         # print(len(contents))
#         for content in contents:
#             # print(content)
#             res.append(content.text)
#         res.pop()
#         ip = ''.join(res)
#
#         port_tag = contents[-1]
#         port_ori_str = port_tag.get('class')[1]
#         # 解码真实的端口
#         port = 0
#         for c in port_ori_str:
#             port *= 10
#             port += (ord(c) - ord('A'))
#         port /= 8
#         port = int(port)
#         print(f'ip:{ip}, port:{port}')
#         return ip, str(port)
#
#     def _judge_proxy_type(self, type_str: str):
#         type_low = type_str.lower()
#         if type_low == 'http':
#             return ProxyTypeEnum.HTTP
#         elif type_low == 'https':
#             return ProxyTypeEnum.HTTPS
#         else:
#             return ProxyTypeEnum.UNKNOWN
#
#     def _judge_proxy_cover(self, cover_str: str):
#         if cover_str == '透明':
#             return ProxyCoverEnum.TRANSPARENT
#         elif cover_str == '高匿':
#             return ProxyCoverEnum.HIGH_COVER
#         else:
#             return ProxyCoverEnum.UNKNOWN
#
#
# @spider_register
# class SpiderXiciIp(AbsSpider):
#     """
#     西刺代理爬虫 刷新速度:🐌慢
#     https://www.xicidaili.com/
#     """
#     def __init__(self) -> None:
#         super().__init__('西刺IP代理爬虫')
#         self._base_urls = [
#             'https://www.xicidaili.com/nn',     # 高匿
#             'https://www.xicidaili.com/nt'      # 透明
#             ]
#
#     async def do_crawl(self) -> Iterable[ProxyEntity]:
#         for base_url in self._base_urls:
#             for page in range(1, 4):
#                 res = requests.get(f'{base_url}/{page}', headers=HEADERS)
#                 soup = BeautifulSoup(res.text, 'lxml')
#                 tr_list = soup.find('table', attrs={'id': 'ip_list'}).find_all('tr')[1: -1]
#                 for tr in tr_list:
#                     tds = tr.find_all('td')
#                     # country = tds[0].find('img')['alt']
#                     ip = tds[1].text
#                     port = tds[2].text
#                     city = tds[3].text.replace('\n', '')
#                     proxy_cover = tds[4].text
#                     proxy_type = tds[5].text
#                     yield ProxyEntity(ip, port,
#                                   source=self._name,
#                                   proxy_cover=self._judge_proxy_cover(proxy_cover),
#                                   proxy_type=self._judge_proxy_type(proxy_type),
#                                   )
#
#     def _judge_proxy_cover(self, cover_str: str):
#         if cover_str == '高匿':
#             return ProxyCoverEnum.HIGH_COVER
#         if cover_str == '透明':
#             return ProxyCoverEnum.TRANSPARENT
#         else:
#             return ProxyCoverEnum.UNKNOWN
#
#     def _judge_proxy_type(self, type_str: str):
#         if type_str == 'HTTPS':
#             return ProxyTypeEnum.HTTPS
#         if type_str == 'HTTP':
#             return ProxyTypeEnum.HTTP
#         else:
#             return ProxyTypeEnum.UNKNOWN

# if __name__ == '__main__':
#     print(isinstance(Spider66Ip().do_crawl(), Coroutine))