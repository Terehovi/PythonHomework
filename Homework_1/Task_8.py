print('Введите длину шоколадки:')
n = int(input())
print('Введите ширину шоколадки:')
m = int(input())
print('Введите количество нужных долек:')
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Yes')
else:
    print('No')