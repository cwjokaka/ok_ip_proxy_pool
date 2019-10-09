class AbsDatabase(object):

    def add_proxy(self, proxy):
        raise NotImplementedError

    def get_all_proxies(self):
        raise NotImplementedError

    def get_unknown_anonymity_proxies(self):
        raise NotImplementedError

    def increase_reliability(self, url):
        raise NotImplementedError

    def reduce_reliability(self, url):
        raise NotImplementedError

    def update_anonymity(self, url, value):
        raise NotImplementedError

    def remove(self, key):
        raise NotImplementedError

    def remove_all_zero_reliability(self):
        raise NotImplementedError

    def init_db(self):
        return
