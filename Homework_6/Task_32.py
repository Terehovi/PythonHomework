import random

size = int(input("Введите размер списка: "))
my_list = [random.randint(1, 100) for _ in range(size)]
print(*my_list)
min_value = int(input("Введите минимум диапазона: "))
max_value = int(input("Введите максимум диапазона: "))

for i in range(0, size):
    if my_list[i] in range(min_value, max_value):
        print(i)