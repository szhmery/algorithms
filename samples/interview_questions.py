import datetime


def print_directory_contents(s_path):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    """
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)


# def singleton(cls):
#     instances = {}
#
#     def wrapper(*args, **kwargs):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return wrapper
#
#
# @singleton
# class Foo(object):
#     pass
#
#
# foo1 = Foo()
# foo2 = Foo()
# print("Decorator way:")
# print(foo1 is foo2)  # True


# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#
# class Foo(Singleton):
#     pass
#
#
# foo1 = Foo()
# foo2 = Foo()
# print("New Base class way:")
# print(foo1 is foo2)  # True


class Singleton(type):

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=Singleton):
    pass


foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2)  # True


def dayofyear():
    year = input("请输入年份:  ")
    month = input("请输入月份:  ")
    day = input("请输入天:   ")
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    return (date1 - date2).days + 1


def str2dict(str1):
    dict1 = {}
    for iterms in str1.split('|'):
        key, value = iterms.split(':')
        dict1[key] = int(value)
    return dict1


def str2dict2(str1):
    # 字典推导式
    d = {k: int(v) for t in str1.split("|") for k, v in (t.split(":"),)}
    return d


def get_files(dir, suffix):
    res = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    print(res)


def pick(obj):
    if obj.endswith(".pyc"):
        print(obj)


def scan_path(ph):
    file_list = os.listdir(ph)
    for obj in file_list:
        if os.path.isfile(obj):
            pick(obj)
        elif os.path.isdir(obj):
            scan_path(obj)


from glob import iglob


def glob_func(fp, postfix):
    for i in iglob(f"{fp}/	/  {postfix}", recursive=True):
        print(i)


import os
from multiprocessing import Process
import time


def pro_func(name, age, **kwargs):
    for i in range(5):
        print("子进程正在运行中，name=%s,age=%d,pid=%d" % (name, age, os.getpid()))
        print(kwargs)
        time.sleep(0.2)


if __name__ == '__main__':
    # print_directory_contents("/Users/sunzhaohui/PycharmProjects/leetcode")
    # whichday = dayofyear()
    # print(whichday)
    str1 = "k:1|k1:2|k2:3|k3:4"
    result = str2dict(str1)
    print(result)
    result = str2dict2(str1)
    print(result)
    print([x * 11 for x in range(10)])

    path = "/Users/sunzhaohui/PycharmProjects/samples"
    get_files(path, '.py')
    scan_path(path)
    glob_func(path, '.py')

    # 创建Process对象
    p = Process(target=pro_func, args=('小明', 18), kwargs={'m': 20})
    # 启动进程
    p.start()
    time.sleep(1)
    # 1秒钟之后，立刻结束子进程
    p.terminate()
    p.join()
