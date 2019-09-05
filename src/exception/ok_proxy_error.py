class OkProxyError(RuntimeError):

    def __init__(self, msg) -> None:
        self._msg = msg
