def Exponentiation(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * Exponentiation(a, b - 1))

num = int(input("Введите число: "))
exp = int(input("Введите показатель степени числа: "))
print(f"Ответ: {Exponentiation(num, exp)}")