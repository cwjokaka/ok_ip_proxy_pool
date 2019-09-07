from src.enum.common import ProxyTypeEnum, ProxyCoverEnum


class ProxyEntity(object):
    """
    ip代理对象
    :param ip ip地址
    :param port 端口
    :param source 代理源头网站名
    :param proxy_type 代理类型 {@link ProxyType}
    :param proxy_cover 代理隐蔽性 {@link CoverOfProxy}
    :param check_count 有效性检验的次数
    :param last_check_time 最后进行有效性检验的时间
    """
    def __init__(self, ip: str, port: str,
                 source: str = 'unknown',
                 supplier = 'unknown',
                 proxy_type: ProxyTypeEnum = ProxyTypeEnum.UNKNOWN,
                 proxy_cover: ProxyCoverEnum = ProxyCoverEnum.UNKNOWN,
                 check_count=0, region='', last_check_time=None):
        self._ip = ip
        self._port = port
        self._source = source
        self._supplier = supplier
        self._proxy_type = proxy_type
        self._proxy_cover = proxy_cover
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
    def supplier(self):
        return self._supplier

    @property
    def proxy_type(self):
        return self._proxy_type

    @property
    def check_count(self):
        return self._check_count

    @property
    def region(self):
        return self._region

    @property
    def last_check_time(self):
        return self._last_check_time
