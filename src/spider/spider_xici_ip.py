from typing import List, Iterable

import requests

from src.entity.proxy_entity import ProxyEntity
from src.enum.common import ProxyCoverEnum, ProxyTypeEnum
from src.spider.abs_spider import AbsSpider
from bs4 import BeautifulSoup
from setting import HEADERS


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

    def do_crawl(self) -> List[ProxyEntity]:
        result = []
        for base_url in self._base_urls:
            for page in range(1, 2):
                res = requests.get(f'{base_url}/{page}', headers=HEADERS)
                soup = BeautifulSoup(res.text, 'lxml')
                tr_list = soup.find('table', attrs={'id': 'ip_list'}).find_all('tr')[1: -1]
                for tr in tr_list:
                    tds = tr.find_all('td')
                    # country = tds[0].find('img')['alt']
                    ip = tds[1].text
                    port = tds[2].text
                    city = tds[3].text
                    proxy_cover = tds[4].text
                    proxy_type = tds[5].text
                    result.append(ProxyEntity(ip, port,
                                              source=self._name,
                                              proxy_cover=self._judge_proxy_cover(proxy_cover),
                                              proxy_type=self._judge_proxy_type(proxy_type),
                                              ))
        return result

    def _judge_proxy_cover(self, cover_str: str):
        if cover_str == '高匿':
            return ProxyCoverEnum.HIGH_COVER
        if cover_str == '透明':
            return ProxyCoverEnum.TRANSPARENT
        else:
            return ProxyCoverEnum.UNKNOWN

    def _judge_proxy_type(self, type_str: str):
        if type_str == 'HTTPS':
            return ProxyTypeEnum.HTTPS
        if type_str == 'HTTP':
            return ProxyTypeEnum.HTTP
        else:
            return ProxyTypeEnum.UNKNOWN