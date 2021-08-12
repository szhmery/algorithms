from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("before executing a_func")
        a_func()
        print("after executing a_func")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration")

print(a_function_requiring_decoration.__name__)