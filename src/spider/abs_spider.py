class AbsSpider(object):

    def __init__(self, name='unknown') -> None:
        self._name = name

    def crawl(self):
        print('开始爬取...')
        self.do_crawl()
        print('爬取完毕!')

    def do_crawl(self):
        raise RuntimeError('do_crawl方法没有实现!')
