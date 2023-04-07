print('Введите номер билета (6 знаков):')
ticket = int(input())
m = []
while ticket > 0:
    element = ticket % 10
    m.append(element)
    ticket //= 10
if m[0] + m[1] + m[2] == m[3] + m[4] + m[5]:
    print('Yes')
else:
    print('No')
