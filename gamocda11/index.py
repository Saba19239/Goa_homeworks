# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სია და დაბეჭდე ამ სიიდან მხოლოდ ლუწი რიცხვები
print("დავალება 1")

def even_numbers(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)

even_numbers([1, 2, 3, 4, 5, 6])

# 2)შექმენი ფუნქცია რომელსაც გადაეცემა სია და დაბეჭდე ამ სიიდან პირველი შემხვედრი ლუწი რიცხვი 
print("დავალება 2")

def first_even(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)
            break

first_even([1, 3, 5, 8, 10])
# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სია და დაბეჭდე სიიდნ 10-ზე დიდი რიცხვების ჯამი და რაოდენობა 
print("დავალება 3")

def numbers_sum(numbers):
    summ = 0
    count = 0

    for i in numbers:
        if i > 10:
            summ += i
            count += 1

    print(summ)
    print(count)


numbers_sum([5, 12, 15, 3, 20])

# 4)შექმენი ფუნქცია რომელსაც გადაეცემა სია და დაბეჭდე ამ სიიდან ყველა რიცხვი რომელიც იყოფა 3-ზე და 5-ზე 
print("დავალება 4")

def devide(nums):
    for i in range(1, 1001):
        if i % 3 == 0 and i % 5 ==0:
            print(i)

print(devide([10, 15, 20, 30, 45, 50]))

# 5)შექმენი ფუნქცია რომელსაც გადაეცემა სია დაბეჭდე ამ სიის ჯამი
print("დავალება 5")

def total_sum(numbs):
    k = 0
    for i in numbs:
        k += i

    print(k)

total_sum([1, 2, 3, 4, 5])
