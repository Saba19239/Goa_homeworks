# 1) 
def greet(name):
    print("Hello World!")
    print(f"Hello {name}")



greet("Saba")


# 2)
def double(number):
    return number ** 2


print(double(67))


# 3)
def checkOdd(number):
    if number % 2 == 0:
        return "ლუწი"
    else:
        return "კენტი"


print(checkOdd(8))
print(checkOdd(7))


# 4)
def BMI(height, weight):
    return weight / (height * height)

height = float(input("შეიყვანე სიმაღლე: "))
weight = float(input("შეიყვანე წონა: "))

print(BMI(height, weight))


# 5)
def getNameByUpper(name):
    return name.upper()


user_name = input("შეიყვანე შენი სახელი: ")
print(getNameByUpper(user_name))