from typing import List

from src.entity.proxy_entity import ProxyEntity


class AbsSpider(object):

    def __init__(self, name='unknown') -> None:
        self._name = name

    def crawl(self):
        print(f'{self._name}开始爬取...')
        res = self.do_crawl()
        print(f'{self._name}爬取完毕!共:{len(res)}个代理')
        # todo 持久化到数据库

        return res

    def do_crawl(self) -> List[ProxyEntity]:
        raise RuntimeError('do_crawl方法没有实现!')

