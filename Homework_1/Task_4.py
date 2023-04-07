print('Введите общее количество поделок:')
count = int(input())
for p in range(0, count):
    for k in range(0, count):
        for s in range(0, count):
            if p == s and p + k + s == count:
                if p + s == k // 2:
                    print(p, k, s)

            
