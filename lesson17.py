def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result

    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper

@print_info
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

@print_info
@print_more
def sub_num(a, b):
    return a - b

r2 = sub_num(10, 20)
print(r2)
# f = print_info(add_num)

# r = f(10, 20)
# print(r)

# print('start')
# r = add_num(10, 20)
# print('end')
# print(r)