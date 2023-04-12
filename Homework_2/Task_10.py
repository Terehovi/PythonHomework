# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

count_zero = 0
count_one = 0
money_count = int(input('Введите количество монет: '))
for i in range(0, money_count):
    x = int(input('Введите 1 или 0: '))
    if x == 0: count_zero += 1
    else: count_one += 1
if count_one > count_zero: print(count_zero)
elif count_zero or count_one == 0: print(0)
else: print(count_one)