from enum import Enum, unique


@unique
class ProxyTypeEnum(Enum):
    UNKNOWN = 0
    HTTP = 1
    HTTPS = 2
    HTTP_AND_HTTPS = 3


@unique
class ProxyCoverEnum(Enum):
    UNKNOWN = 0
    TRANSPARENT = 1
    NORMAL_COVER = 2
    HIGH_COVER = 3
