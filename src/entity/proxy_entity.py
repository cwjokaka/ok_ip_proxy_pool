from src.enum.common import ProxyTypeEnum, ProxyCoverEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from setting import DB
Base = declarative_base()


class ProxyEntity(Base):
    __tablename__ = DB['table_name']
    url = Column(String(36), primary_key=True)
    # ip = Column(String(20))
    # port = Column(String(5))
    source = Column(String(16))
    # protocol = Column(String(5))
    supplier = Column(String(16))
    proxy_type = Column(Integer())
    proxy_cover = Column(Integer())
    check_count = Column(Integer())
    region = Column(String(32))
    last_check_time = Column(String(32))
    reliability = Column(Integer())

    """
    ip代理对象
    :param url url地址
    :param ip ip地址
    :param port 端口
    :param protocol 协议
    :param source 代理源头网站名
    :param proxy_type 代理类型 {@link ProxyType}
    :param proxy_cover 代理隐蔽性 {@link CoverOfProxy}
    :param check_count 有效性检验的次数
    :param last_check_time 最后进行有效性检验的时间
    :param reliability 代理可靠性, 默认为5
    """
    def __init__(self, url: str,
                 # ip: str,
                 # port: str,
                 # protocol: str = 'http',
                 source: str = 'unknown',
                 supplier='unknown',
                 proxy_type: int = ProxyTypeEnum.UNKNOWN.value,
                 proxy_cover: int = ProxyCoverEnum.UNKNOWN.value,
                 check_count=0, region='', last_check_time=None, reliability=5):
        self.url = url
        # self.ip = ip
        # self.port = port
        # self.protocol = protocol
        self.source = source
        self.supplier = supplier
        self.proxy_type = proxy_type
        self.proxy_cover = proxy_cover
        self.check_count = check_count
        self.region = region
        self.last_check_time = last_check_time
        self.reliability = reliability
