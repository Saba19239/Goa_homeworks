# 1)შექმენი ფუნქცია რომელსაც გაადეცემა სია და დაბეჭდე სიის სიგრძე ანუ რამდენი ელემენტია 
def length(leng):
    return len(leng)

print(length([1, 2, 3, 4, 5]))
# 2)შექმენი ფუნქცია რომელსაც გადაეცემა სია და დაბეჭდე ამ სიიდან ყველა რიცხვის ჯამი რომელიც არის 30-ზე მეტი ასევე რაოდენობა 
def numbers_sum(numbers):
    summ = 0
    count = 0

    for i in numbers:
        if i > 30:
            summ += i
            count += 1

    print(summ)
    print(count)

numbers_sum([25, 35, 40, 15, 55])
# 3) შექმენი ფუნქცია რომელსაც გადაეცემა სია დააბრუნე კენტი რიცხვების ჯამი და რაოდენობა 
def odd_numbers(nums):
    sumn = 0
    countt = 0

    for i in nums:
        if i % 2 != 0:
            sumn += i
            countt += 1

    return sumn, countt

print(odd_numbers([5, 9, 14, 7, 4, 8]))

# 4)შექმენი ფუნქცია რომელსაც გადაეცემა სია ამოიღე ამ სიიდან 4- ელემენტი 
def remove(lest):
    lest = lest[3::3]
    print(lest)

remove(["blue", "red", "yellow", "green", "orange"])


# 5)შეინახე ცვლადში რიცხვი მომხმარებელს იქამდე სემოაყვანინე რიცხვი სანა სწორს არ შეიყვანს 
num = 8
user_num = 0

while user_num != num:
    user_num = int(input("Wrong, enter new number: "))

print("Correct!")

# 6)შექმენი სია და გააკეთე ასლი 
my_list = [1, 2, 3, 4, 5]

copy_list = my_list

print(copy_list)

# 7)კომენტარის სახინ ახსენი რა არის ციკლები

#ციკლები საშუალებას გვაძლევს ერთი და იგივე ქმედება რამდენჯერმე შევასრულოთ, python-ში არის ორი ციკლი, For და While ციკლ~/