from src.enum.common import ProxyTypeEnum, ProxyCoverEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class ProxyEntity(Base):
    # 指定本类映射到users表
    __tablename__ = 'proxy'
    # 指定id映射到id字段; id字段为整型，为主键
    id = Column(Integer, primary_key=True)
    # 指定name映射到name字段; name字段为字符串类形，
    ip = Column(String(20))
    port = Column(String(5))
    source = Column(String(16))
    supplier = Column(String(16))
    proxy_type = Column(Integer())
    proxy_cover = Column(Integer())
    check_count = Column(Integer())
    region = Column(String(32))
    last_check_time = Column(String(32))

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
                 supplier='unknown',
                 proxy_type: int = ProxyTypeEnum.UNKNOWN.value,
                 proxy_cover: int = ProxyCoverEnum.UNKNOWN.value,
                 check_count=0, region='', last_check_time=None):
        self.ip = ip
        self.port = port
        self.source = source
        self.supplier = supplier
        self.proxy_type = proxy_type
        self.proxy_cover = proxy_cover
        self.check_count = check_count
        self.region = region
        self.last_check_time = last_check_time
