num_list = [0, 1, 2, 3, 4, 5 ,6 , 7, 8, 9]

for i in num_list:
    print(i)

for i in range(10):
    print(i)

for i in range(2, 10):
    print(i)

for i in range(2, 10, 3):
    print(i)

for _ in range(10):
    print(i, 'hello')

i = 0
for fruit in ['Apple', 'Banana', 'Orange']:
    print(i, fruit)
    i += 1

for i, fruit in enumerate(['Apple', 'Banana', 'Orange']):
    print(i, fruit)