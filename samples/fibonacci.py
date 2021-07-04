def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fib_test(n):
    ans = []
    for i in range(n):
        ans.append(fibonacci_recursive(i))
    return ans

if __name__ == '__main__':

    result = fib_test(6)
    print(result)

def fibonacci_iterative(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci(n):
    def fib(n_, s):
        if n_ == 0:
            return s[0]
        a, b = s
        return fib(n_ - 1, (b, a + b))

    return fib(n, (1, 1))


def fibs():
    yield 1
    fibs_ = fibs()
    yield next(fibs_)
    fibs = fibs()
    for fib in map(lambda a, b: a + b, fibs_, fibs):
        yield fib


def fibonacci(n):
    fibs_ = fibs()
    for _ in range(n):
        next(fibs_)
    return next(fibs)


def cache(fn):
    cached = {}

    def wrapper(args):
        if args not in cached:
            cached[args] = fn(args)
            return cached[args]

        wrapper.name = fn.name
        return wrapper


@cache
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)
