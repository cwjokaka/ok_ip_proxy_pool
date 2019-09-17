from typing import List

from src.entity.proxy_entity import ProxyEntity


class AbsSpider(object):

    def __init__(self, name='unknown') -> None:
        self._name = name

    async def crawl(self):
        res = []
        print(f'{self._name}开始爬取...')
        try:
            res.extend(await self.do_crawl())
            # print(f'{self._name}爬取完毕!共:{len(res)}个代理')
        except Exception as e:
            print(f'{self._name}爬取失败:e:{e}')
        return res

    async def do_crawl(self) -> List[ProxyEntity]:
        raise NotImplementedError

