print('Введите общее количество поделок:')
count = int(input())
for peter in range(0, count):
    for kate in range(0, count):
        for sergey in range(0, count):
            if peter == sergey and peter + kate + sergey == count:
                if peter + sergey == kate// 2:
                    print(peter, kate, sergey)

            
