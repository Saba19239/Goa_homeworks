# 1)for loop გამოყენებით 1,20 მდე ყველა რიცხვის ჯამი გამოთვალე 
sum = 0


for i in range(1, 21):
    sum += i

print(sum)

# 2)1-50 მდე დაითვალე რამდენი ლუწი რიცხვია
count = 0

for i in range(1, 51):
    if i % 2 ==0:
        count += 1

print(count)

# 3)მომხმარებელს შემოაყვანინე რიცხვი და გამოთვალე მისი ციფრების ჯამი 
numb = int(input("Enter your number: "))
sumb = 0

while numb > 0:
    sumb += numb % 10
    numb //= 10

print(sumb)
# 4)შექმენი სია რომელშიც იქნება დადებითი და უარყოფითი რიცხვები დააბრუნე ახალი სია სადაც მხოლოდ დადებითი რიცხვები იქნება 
sia = [5, -3, 8, -2, 10, -7]
upd_sia = []

for i in sia:
    if i > 0:
        upd_sia.append(i)

print(upd_sia)

# 5)შექმენი ფუნქცია რომელსაც გადაეცემა 2 რიცხვი დააბრუნე მათი ნამრავლი 

def mult(x, y):
    return x * y

print(mult(2, 6))

# 6)1-1000 მდე დაბეჭდე მხოლოდ ის რიცხვები რომელიც იყოფა 3-ზე და 5-ზე

for i in range(1, 1001):
    if i % 3 == 0 and i % 5 ==0:
        print(i)

# 7)while loop გამოყენებით დაბეჭდე 10-დან 1-ადე
i = 10

while i >= 1:
    print(i)
    i -= 1

# 8)შექმენი სია და იპოვე უდიდესი რიცხვი არ გამოიყენო max 
lista = [5, 12, 3, 25, 8]
big_num = lista[1]

for i in lista:
    if i > big_num:
        big_num = i

print(big_num)

# 9)შექმენი ფუნქცა რომელსაც გადაეცემა სახელი თუ სახელის სიგრძე მეტია 5-ზე დააბრუნე True სხვა შემთხვევაში False 

def name(sda):
    if len(sda) > 5:
        return True
    else:
        return False

print(name("jake"))

# 10)1 დან 50 მდე გამოთვალე ყველა კენტი რიცხვის ჯამი 
jami = 0

for i in range(1, 51):
    if i % 2 != 0:
        jami += i

print(jami)

# 11)შექმენი სია და დაბეჭდე ახალი სია რომელშიც მხოლოდ ის რიცხვები იქნება რომელიც არის 10-ზე მეტი 
lesta = [5, 15, 8, 20, 3, 30]
new_lesta =  []

for i in lesta:
    if i > 10:
        new_lesta.append(i)

print(new_lesta)

# 12)შეინახე რიცხვი, მომხმარებელს იქამდე შემოაყვანინე რიცხვი სანამ სწორს არ გამოიცნობს 
correct = 7

n = int(input("Guess the number: "))

while n != correct:
    n = int(input("Try again: "))

print("Correct!")

# 13)შექმენი ფუნქცია რომელსაც გადაეცმე სია და დაბეჭდე ამ სიიდან პირველი შემხვედრი ლუწი რიცხვი 
def even(siaa):
    for i in siaa:
        if i % 2 == 0:
            return i
            
siaa = [3, 5, 7 ,8]

# 14)1-100 მდე გამოთვალე 5-ის ჯერადი რიცხვები 
sumn = 0

for i in range(1, 101):
    if i % 5 == 0:
        sumn += i

print(sumn)

# 15)შექმენი ფუნქცია რომელსაც გადაეცემა სია და დააბრუნე სიის ჯამი არ გამოიყენო sum

def jamiii(listt):
    summm = 0

    for i in listt:
        summm += i

    return summm

print(jamiii([5, 10, 15, 20]))