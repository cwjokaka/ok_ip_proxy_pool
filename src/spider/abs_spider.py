from typing import List

from src.entity.proxy_entity import ProxyEntity


class AbsSpider(object):

    def __init__(self, name='unknown') -> None:
        self._name = name

    def crawl(self):
        print(f'{self._name}开始爬取...')
        try:
            res = self.do_crawl()
            print(f'{self._name}爬取完毕!共:{len(res)}个代理')
        except Exception as e:

            return []
        return res

    def do_crawl(self) -> List[ProxyEntity]:
        raise NotImplementedError

