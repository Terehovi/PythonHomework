game = {"AEIOULNSTRАВЕИНОРСТ": 1, "DGДКЛМПУ": 2, "BCMPБГЁЬЯ": 3,
        "FHVWYЙЫ": 4, "KЖЗХЦЧ": 5, "JXШЭЮ": 8, "QZФЩЪ": 10}

word = input("Введите слово: ")
score = 0
for letter in word.upper():
    for letters in game.keys():
        if letter in letters:
            score += game.get(letters)
            break
print(score)