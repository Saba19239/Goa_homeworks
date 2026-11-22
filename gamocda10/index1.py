# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სახელი ფუნქციამ დააბრუნოს 1 ასოს და ბოლო ასოს გარესე სახელი 
def saxeli(name):
    return name[1:-1]

print(saxeli("Giorgi"))

# 2)შექმენი ფუნქცია რომლსაც გადაეცემა რიცხვი ფუნქციამ უნდა დააბრუნო ეს რიცხვები თითოეული რიცხვი გამრავლებილი თავის თავზე 
def squere(numbers):
    liste = ""

    for i in str(numbers):
        liste += str(int(i) * int(i))

    return int(liste)

print(squere(5))

# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სიტყვა და დააბრუნოს ხმოვანი ასოების რაოდენობა "aeiou" 
def vowel(word):
    count = 0

    for i in word:
        if i in "aeiou":
            count += 1

    return count

print(vowel("animal"))


# 4)შექმენი ფუნქცია რომელსაც გადაეცემა ტეხსტი და დააბრუნე შეტრიალებული ტექსტი 
def reverse(text):
    return text[::-1]

print(reverse("hello"))

# 5)შექმენი ფუნქცია რომელსაც გადაეცემა სია დააბრუნე იმ რიცხვების ჯამი რომელიც მეტია 4-ზე
def sum(sia):
    toptal = 0

    for i in sia:
        if i > 4:
            toptal += i

    return toptal

print(sum([2, 5, 8, 10]))