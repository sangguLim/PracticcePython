def sum_with_plus_decorator(arg):

    def inner(func):
        def core(values):
            return reduce(func, values, power)
        return core
    if callable(arg):
        power = 0
        return inner(arg)
    else:
        power = arg
        return inner


@sum_with_plus_decorator
def add_together(a, b):
    return a + b


print(add_together([1, 3, 11, 33, 31, 13, 21, 32, 51, 35]))