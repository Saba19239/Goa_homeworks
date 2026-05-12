# 9) დაბეჭდეთ 0-დან 100-ის ჩათვლით ყველა რიცხვი. (for-თაც და while-თაც)

# 10) დაბეჭდეთ 10-დან 20-მდე ყველე რიცხვი (for-თაც და while-თაც)

# 11) დაბეჭდეთ 100-დან 200-ის ჩათვლით ყოველი მე-5 რიცხვი (for-თაც და while-თაც)

# 12) დაბეჭდეთ 10-დან 0-ის ჩათვლით ყველა რიცხვი (for-თაც და while-თაც)

# 9 (for)
for i in range(0, 101):
    print(i)

# 9 (while)
i = 0
while i <= 100:
    print(i)
    i += 1


# 10 (for)
for i in range(10, 21):
    print(i)

# 10 (while)
i = 10
while i <= 20:
    print(i)
    i += 1


# 11 (for)
for i in range(100, 201, 5):
    print(i)

# 11 (while)
i = 100
while i <= 200:
    print(i)
    i += 5


# 12 (for)
for i in range(10, -1, -1):
    print(i)

# 12 (while)
i = 10
while i >= 0:
    print(i)
    i -= 1