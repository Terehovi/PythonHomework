import random

size = int(input('Введите размер списка: '))
my_list = []
for i in range(0, size):
    my_list.append(random.randint(1, 10))
print(my_list)

num = int(input('Введите число: '))
print(my_list.count(num))