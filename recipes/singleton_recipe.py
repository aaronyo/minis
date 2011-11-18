def only_once(f):
    def new__init__(self, *args, **kwargs):
        assert(f.__name__ == '__init__')
        if self._instance:
            raise Exception("You can only call '%s.%s' once" \
                            % (self.__class__.__name__, f.__name__))
        else:
            return f(self, *args, **kwargs)
    return new__init__

class MySingleton(object):

    _instance = None

    @only_once
    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = MySingleton()
        return cls._instance


s1 = MySingleton.get_instance()
s2 = MySingleton.get_instance()
print s1
print s2
MySingleton()
