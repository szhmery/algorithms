# coding = utf-8

class DBManager(object):
    def __init__(self):
        pass

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        return True


def getInstance():
    return DBManager()


# sample from Python Programming
class TraceBlock():
    def __init__(self):
        print("Initiating...")

    def message(self, arg):
        print("running...", arg)

    def __enter__(self):
        print("Starting the block, enter...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print("raise an exception", exc_type)
            print(exc_type)
            print(exc_tb)
            return False
        else:
            print("Exist normally.")


with TraceBlock() as action:
    action.message("test 1")
    print('reached')

with TraceBlock() as action:
    action.message("test 2")
    raise TypeError
    print("not reached")
