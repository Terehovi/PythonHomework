import random

def Sorting(list):
    for i in range(0, len(list) - 1):
        for j in range(len(list) - 1):
            if (list[j] > list[j + 1]): 
                    temp = list[j] 
                    list[j] = list[j + 1] 
                    list[j + 1] = temp
    return list

size_1 = int(input('Введите размер первого списка: '))
size_2 = int(input('Введите размер второго списка: '))
print()

my_list_1 = []
my_list_2 = []

for i_1 in range(0, size_1):
    my_list_1.append(random.randint(1, 20))

for i_2 in range(0, size_1):
    my_list_2.append(random.randint(1, 20))

print(my_list_1)
print(my_list_2)
print()

my_list_1 = set(Sorting(my_list_1))
my_list_2 = set(Sorting(my_list_2))

print(my_list_1)
print(my_list_2)
print()


print(my_list_1.intersection(my_list_2))

