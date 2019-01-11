def say_something():
    print('hi')

say_something()

def say_anything():
    s = 'hi'
    return s

print(say_anything())

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return 'I don\'t know'


result = what_is_this('red')
print(result)

def add_num(a: int, b: int) -> int:
    return a + b

result = add_num('10', '20')
print(result)