def say_something(word, *args):
    print(word, ',')
    for str in args:
        print(str)

say_something("hi", "Mike", "Nancy")

t = ('Mike', 'Nancy')
say_something("Hi", *t)

print('###############################')

def menu(**kwargs):
    print(kwargs)

    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

dic = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'desert': 'ice cream',
}
menu(**dic)

print('###############################')
def menu(food, *args, **kwargs):
    print(food)
    for item in args:
        print(item)
    for k, v in kwargs.items():
        print(k, v)

menu('banana', 'apple', 'orange', entree="beef", drink="coffee")