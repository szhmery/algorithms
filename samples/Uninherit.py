#https://blog.csdn.net/weixin_28885791/article/details/115995363
class Father(object):
    def __new__(cls, *args, **kwargs):
        if cls != Father:
            raise Exception("You should not inherit this class. Got subclass(es): " + str(Father.__subclasses__()))
        return super(Father, cls).__new__(cls)

    def __init__(self, x):
        self.val = x


class Son(Father):
    def __init__(self, x):
        self.val = x


Father(10)
Son(10)
