class AbsDatabase(object):

    def set(self, key, value):
        raise RuntimeError('该set方法未实现!')

    def get(self, key):
        raise RuntimeError('该get方法未实现!')

    def remove(self, key):
        raise RuntimeError('该remove方法未实现!')
