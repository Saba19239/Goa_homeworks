# 2) კომენტარების სახით ახსენით რა არის input-ი და output-ი, მოიყავნეთ შესაბამისი მაგალითები.

# 3) შექმენით ცვლადი, რომელშიც შეინახავთ input ინსტრუქციით შემოტანილ მნიშვნელობას, შემდეგ შეამოწმებთ თუ რა ტიპის მონაცემი ინახება ამ ცვლადში და დაპრინტავთ.

# 4) თიოთეული მონაცემთა ტიპისთვის (str,int,float), შექმენით 5 ცვლადი და დაუწერეთ კომენტარი თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.

# 5) აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.

# 6) მომიტყვა, ხმარებელს შემოატანინეთ ორი შეინახეთ ისინი ცვლადებში, მოახდინეთ მათი კონკატინაცია და დაბეჭდეთ.

# პასუხები

#2)

#input - ინფუთი არის ინფორმაცია რასაც პროგრამას გადავცემთ, მაგალითად ჩვენი მიკროფონი ან კლავიატურა და მაუსი
#output- აუთფუთი ნიშნავს ინფორმაციას რასაც პროგრამა გამოსცემს, მაგალითად სპიკერი ანდ მონიტორი

#3)

name = input("insert generic name here: ")

print(type(name))

#4)

#str

name_1 = "goa"
name_2 = "goaa"
name_3 = "goaaa"
name_4 = "goaaaa"
name_5 = "goaaaaa"

#int

num_1 = 10
num_2 = 100
num_3 = 1000
num_4 = 10000
num_5 = 100000

#float

flt_1 = 1.0
flt_2 = 2.0
flt_3 = 3.0
flt_4 = 4.0
flt_5 = 5.0

print(type(name_1))
print(type(name_2))
print(type(name_3))
print(type(name_4))
print(type(name_5))

print(type(num_1))
print(type(num_2))
print(type(num_3))
print(type(num_4))
print(type(num_5))

print(type(flt_1))
print(type(flt_2))
print(type(flt_3))
print(type(flt_4))
print(type(flt_5))

#5)

str = "goa"

print(type(str))

int = 10

print(type(int))

float = 1.0

print(type(float))

#6)

name_1 = input("insert name here: ")

name_2 = input("insert name here: ")

print(name_1 +" "+ name_2)
















