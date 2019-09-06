class ProxyEntity(object):

    def __init__(self, ip: str, port: str, source: str = '', type='', check_count=0, region='', last_check_time=None):
        self._ip = ip
        self._port = port
        self._source = source
        self._type = type
        self._check_count = check_count
        self._region = region
        self._last_check_time = last_check_time

    @property
    def ip(self):
        return self._ip

    @property
    def port(self):
        return self._port

    @property
    def source(self):
        return self._source

    @property
    def type(self):
        return self._type

    @property
    def check_count(self):
        return self._check_count

    @property
    def region(self):
        return self._region

    @property
    def last_check_time(self):
        return self._last_check_time
