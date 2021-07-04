def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
if a1 == a2:
    print(True)
else:
    print(False)


# 使用__new__方法在创造实例时进行干预，达到实现单例模式的目的
# 这里使用了_instance属性来存放实例
class Singleton:  # 一个通用的单例超类，其他类继承即可（也可通过装饰器实现）
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance


class SingleSpam(Singleton):
    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s


s1 = SingleSpam('spam')
print(id(s1), s1)
s2 = SingleSpam('spa')
print(id(s2), s2)
print(s1 is s2)


