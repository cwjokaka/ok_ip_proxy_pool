from src.database.abs_database import AbsDatabase


class MemoryDB(AbsDatabase):
    """
    数据库:基于内存实现
    """
    def __init__(self) -> None:
        self._box = {}

    def put(self, key, value):
        self._box[key] = value

    def get(self, key):
        return self._box[key]

    def remove(self, key):
        return self._box.pop(key, None)


memory_db_instance = MemoryDB()
