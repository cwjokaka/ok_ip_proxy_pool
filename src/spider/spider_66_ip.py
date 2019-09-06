import requests

from src.spider.abs_spider import AbsSpider
from bs4 import BeautifulSoup


class Spider66Ip(AbsSpider):
    """
    66IP代理爬虫
    http://www.66ip.cn/
    """
    def __init__(self) -> None:
        super().__init__('66IP代理爬虫')
        self._base_url = 'http://www.66ip.cn'

    def do_crawl(self):
        for page in range(1, 5):
            print(f'第{page}页...')
            resp = requests.get(f'{self._base_url}/{page}.html')
            resp.encoding = 'gb2312'
            soup = BeautifulSoup(resp.text, 'lxml')
            tr_list = soup.find('table', attrs={'width': '100%', 'bordercolor': '#6699ff'}).find_all('tr')
            for i, tr in enumerate(tr_list):
                if i == 0:
                    continue
                contents = tr.contents
                ip = contents[0].text
                port = contents[1].text
                region = contents[2].text
                proxy_type = contents[3].text
                check_time = contents[4].text
                print(f'{ip}:{port}/{region}/{proxy_type}/{check_time}')
