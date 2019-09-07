from typing import List, Iterable

import requests

from setting import HEADERS
from src.entity.proxy_entity import ProxyEntity
from src.enum.common import ProxyTypeEnum, ProxyCoverEnum
from src.spider.abs_spider import AbsSpider
from bs4 import BeautifulSoup, Tag


class SpiderQuanWangIp(AbsSpider):
    """
    全网IP代理爬虫 刷新速度:极快
    http://www.goubanjia.com/
    """
    def __init__(self) -> None:
        super().__init__('全网IP代理爬虫')
        self._base_url = 'http://www.goubanjia.com'

    def do_crawl(self) -> List[ProxyEntity]:
        result = []
        resp = requests.get(self._base_url, headers=HEADERS)
        soup = BeautifulSoup(resp.text, 'lxml')
        # print(soup.prettify())
        tr_list = soup.find('tbody').find_all('tr')
        for i, tr in enumerate(tr_list):
            tds = tr.find_all('td')
            id_and_port = tds[0]
            ip, port = self._parse_ip_and_port(id_and_port)
            proxy_cover = tds[1].text
            proxy_type = tds[2].text
            region = tds[3].contents[1].text
            supplier= tds[4].text
            # resp_speed = tds[5].text[:-2]
            # last_check_time = tds[6]
            # ttl = tds[7]
            result.append(ProxyEntity(ip, port,
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
        # print(len(contents))
        for content in contents:
            # print(content)
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
        print(f'ip:{ip}, port:{port}')
        return ip, str(port)

    def _judge_proxy_type(self, type_str: str):
        type_low = type_str.lower()
        if type_low == 'http':
            return ProxyTypeEnum.HTTP
        elif type_low == 'https':
            return ProxyTypeEnum.HTTPS
        else:
            return ProxyTypeEnum.UNKNOWN

    def _judge_proxy_cover(self, cover_str: str):
        if cover_str == '透明':
            return ProxyCoverEnum.TRANSPARENT
        elif cover_str == '高匿':
            return ProxyCoverEnum.HIGH_COVER
        else:
            return ProxyCoverEnum.UNKNOWN