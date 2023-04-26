first_element = int(input("Введите первый элемнт прогрессии: "))
step = int(input("Введите шаг прогрессии: "))
element_count = int(input("Введите количество елементов прогрессии: "))
my_list = [first_element]
for i in range(0, element_count - 1):
    first_element += step
    my_list.append(first_element)

print(*my_list)