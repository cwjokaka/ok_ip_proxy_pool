class AbsDatabase(object):

    def add_proxy(self, proxy):
        raise NotImplementedError

    def get_all_proxies(self):
        raise NotImplementedError

    def increase_reliability(self, protocol, ip, port):
        raise NotImplementedError

    def reduce_reliability(self, protocol, ip, port):
        raise NotImplementedError

    def remove(self, key):
        raise NotImplementedError

    def init_db(self):
        return
