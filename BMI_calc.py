# Aidan Zarski

# Pseudocode
# start
# input the height(m)
# input the weight(kg)
# do weight/(height*height) to find BMI
# display BMI
# if BMI is less than 14 say "your underweight"
# elif bmi is greater than 40 say "your overweight"
# else say "your normal"

import os
os.system('cls')

weight = float(input("input your weight(kg)"))
height = float(input("input your height(m)"))

BMI = weight / (height * height)

print("your BMI is",BMI)

if BMI < 14:
    print("your underweight")
elif BMI > 40:
    print("your overweight")    
else:
    print("your normal")