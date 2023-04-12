sum = int(input('Введите сумму загаданных вами натуральных чисел: '))
proizv = int(input('Введите произведение загаданных вами натуральных чисел: '))
if (sum > 0) and (proizv > 0):
    for x in range(1, 1001):
        for y in range(1, 1001):
            if (sum == x + y) and (proizv == x * y):
                print(x, y)
            else: print('Таких натуральных чисел нет')
else: print('Некорректный ввод')