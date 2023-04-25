import random

size = int(input())
my_list = []
for i in range(size):
    my_list.append(random.randint(1, 20))

res = []
for j in range(len(my_list) - 1):
    res.append(my_list[j - 1] + my_list[j] + my_list[j + 1])
res.append(my_list[-2] + my_list[-1] + my_list[0])
print(res)