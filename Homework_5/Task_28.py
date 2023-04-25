def rec_sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return rec_sum(a + 1, b - 1)
    else:
        return rec_sum(a - 1, b + 1)
    
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(f"Ответ: {rec_sum(num1, num2)}")
