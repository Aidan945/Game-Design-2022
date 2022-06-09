import os
os.system('cls')


birth_year = float(input("input your year of birth "))
current_year = float(input("input the current year "))


age = current_year - birth_year
print("your age is",age)

if age > 50:
    print("you are old")
if age <= 50:
    print("you are young")    