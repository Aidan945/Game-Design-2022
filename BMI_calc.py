import os
os.system('cls')

print("hello")

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