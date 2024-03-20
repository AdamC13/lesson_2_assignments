#1
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#2
num1 = int(input("\nGive me a number: "))
num2 = int(input("Give me a number again: "))
num3 = int(input("Give me one more number: "))

lrg_num = None
sm_num = None
lrg_tie = False
sm_tie = False

if num1 >= num2 and num1 >= num3:
    lrg_num = num1
if num2 >= num1 and num2 >= num3:
    if lrg_num == None:
        lrg_num = num2
    else:
        lrg_tie = True
if num3 >= num2 and num3 >= num1:
    if lrg_num == None:
        lrg_num = num3
    else:
        lrg_tie = True

if num1 <= num2 and num1 <= num3:
    sm_num = num1
if num2 <= num1 and num2 <= num3:
    if sm_num == None:
        sm_num = num2
    else:
        sm_tie = True
if num3 <= num2 and num3 <= num1:
    if sm_num == None:
        sm_num = num3
    else:
        sm_tie = True


print(" \nThis is your largest number! " + str(lrg_num))
print("This is your smallest number! " + str(sm_num))
if lrg_tie == True and sm_tie == True:
    print("All numbers are equal!")
elif lrg_tie == True:
    print("There is a tie for the largest number!")
elif sm_tie == True:
    print("There is a tie for the smallest number!")

#3
year = int(input("\nGive me a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year == True:
    print(str(year) + " is a leap year!")
else:
    print(str(year) + " is not a leap year")