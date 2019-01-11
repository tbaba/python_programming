def menu(entree='beef', drink='wine', desert='ice'):
    print(entree)
    print(drink)
    print(desert)
    print('done')

menu(entree='beef', desert='ice', drink='beer')
menu()

def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)

y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
r = test_func(200, y)
print(r)

