class AbsSpider(object):

    def __init__(self, name='unknown') -> None:
        self._name = name

    def crawl(self):
        print('开始爬取...')
        res = self.do_crawl()
        print(f'爬取完毕!共:{len(res)}个代理')
        return res

    def do_crawl(self):
        raise RuntimeError('do_crawl方法没有实现!')
