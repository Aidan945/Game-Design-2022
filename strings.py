#Aidan Zarski
#Learning Strings

from email.headerregistry import MessageIDHeader
import os
os.system('cls')

print('hi')
message = "you are awsome" # a string is an array of characters

print(message)
print(message[5])

wordlength = len(message) # used to calculate the length of a string
print(wordlength)
print(wordlength-1)

if message.isdigit(): # when using methods add a dot
    sum = message + 3
else: # if the statment is false it runs the else statment
    print(message + " i say no") # concatanation   

print(message.upper())
message = message.upper()

if message.isupper():
    print(message)
else:
    message = message.upper()
    print(message)

middle = int(wordlength/2)
print(message[middle + 1])

print(message[0:6])
print(message[7:])

print(help(message.upper))




