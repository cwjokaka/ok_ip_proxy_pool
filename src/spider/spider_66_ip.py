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
        for page in range(1, 2):
            resp = requests.get(f'{self._base_url}/{page}.html')
            resp.encoding = 'gb2312'
            soup = BeautifulSoup(resp.text, 'lxml')
            print(soup.find('table', attrs={'width': '100%', 'bordercolor': '#6699ff'}).find_all('tr'))
            # print(resp.text)
