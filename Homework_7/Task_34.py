def rifm(list1):
    res = 1
    for i in range(0, len(list1) - 1):
        if list1[i].count('а') == list1[i + 1].count('а'):
            res *= 2
        else:
            res *= 0
    if res == 0: print('Пам парам')
    else: print('Парам пам-пам')

my_string = input('Введите строку: ').lower()
my_list = list(my_string.split())
rifm(my_list)
