# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სია იპოვე პირველი შემხვედრი ლუწი რიცხვი თუ სიაში არ არის ლუწი რიცხვი გამოიტანე "ვერ მოიძებნა" 
def find_evn(lst):
    for i in lst:
        if i % 2 == 0:
            print(i)
            break
    else:
        print("ვერ მოიძებნა")

find_evn([1, 3, 4, 8, 7])
    
# 2)შექმენი ფუნქცია რომელსაც გადაეცემა სია და წაშალე ამ სიიდან განმეორებადი რიცხვები თუ სიაში არის ორჯერ 2 წაშალე და დატოვე მხოლოდ 1
def remove_dupe(lsst):
    upd_list = []

    for i in lsst:
        if i not in upd_list:
            upd_list.append(i)

    print(upd_list)

remove_dupe([1, 2, 2, 3, 4, 4, 4, 5])

# 3)იპოვე სიაში მეორე უდიდესი რიცხვი 
def second_larg(lest):


    second_larg([5, 10, 3, 20, 17])

# 4)მომხმარებელს შემოაყვანინე რიცხვი და გამოთვალე ამ რიცხვის ჯამი მაგალითად თუ შემოიყვანს 11 1+1 დაბეჭდე 2 
def digit_sum():
    num = input("Enter number: ")
    total = 0

    for i in num:
        total += int(i)

    print(total)

digit_sum()

# 5)იპოვე სიაში რომელი რიცხვები მეორდება ყველაზე მეტჯერ 
def most_repeat(lost):
    maximum = 0

    for i in lost:
        if lost.count(i) > maximum:
            maximum = lost.count(i)

    for i in lost:
            if lost.count(i) == maximum:
                print(i)
            
most_repeat([1, 2, 2, 3, 4, 4, 4])
# 6)სიაში პირველი ელემენტი გადაიტანე ბოლოში 
def move_element(lust):
    lust.append(lust.pop(0))     
    print(lust)

move_element([1, 2, 3, 4, 5])

# 7)შემენი ფუნქცია რომელსაც დაგაეცემა სია სადაც არის დადებითი და უარყოფითი რიცხვები ამოიღე სიიდან უაროფითი რიცხვები და დააბრუნე დადებითები
def positive_numbers(lyst):
    new_list = []

    for i in lyst:
        if i > 0:
            new_list.append(i)

    return new_list

print(positive_numbers([-2, 5, -6, 4, 8, -3]))