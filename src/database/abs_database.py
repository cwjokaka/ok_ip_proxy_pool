class AbsDatabase(object):

    def put(self, key, value):
        raise RuntimeError('该put方法未实现!')

    def get(self, key):
        raise RuntimeError('该get方法未实现!')

    def remove(self, key):
        raise RuntimeError('该remove方法未实现!')
