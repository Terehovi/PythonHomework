import random

counter = 0
size = int(input('Введите размер списка: '))
my_list = []
for i in range(0, size):
    my_list.append(random.randint(-10, 10))
print(my_list)

blizk = my_list[0]

num = int(input('Введите число: '))
if num in my_list: 
    print(f"Число {num} встречается {my_list.count(num)} раз(а)")
else: 
    if my_list.count(num) == 0:
        for item in my_list:
            if abs(num- blizk) > abs(num - item):
                blizk = item
        print(f"Числа {num} тут нет! Бизжайшее к ниму число {blizk}")