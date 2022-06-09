# Aidan Zarski
# Checks if a number is even, odd, a multiple of 3, or a multiple of 5

import os
os.system('cls')
num = int(input("Enter a number: "))
if (num%2 == 0):
    print("even")
else:
    print("odd")
if num%3==0:
    print("multpiple of 3")
if num%5==0:
    print("multpiple of 5")