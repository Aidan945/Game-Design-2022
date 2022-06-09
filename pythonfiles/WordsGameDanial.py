# Daniel Walker
# from ctypes.wintypes import WORD
import random
import os, datetime

os.system ('cls')

list1 = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
list2 = ["red", "blue", "yellow", "green", "orange", "purple", "indigo", "black", "white", "brown"]
list3 = ["Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry", "Cherry", "Coconut", "Cucumber", "Durian"]
count = 0
Game = True
theword = ""
high = 0
name = input("What is your name? ")

def hint(): # allows us to reuse code in multiple spots
    global count
    if count == 0:
        print("|*************************************|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|        only 2 shells in fact        |")
        print("|*************************************|")
        
    elif count == 1:
        print("|**************************************|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|**************************************|")
    
    else:
        print("You are horrible at guessing, no more hints, go till you get it right")

def selectWord(choice):
    global theword
    if choice == 1:
        theword = random.choice(list1)
    if choice == 2:
        theword = random.choice(list2)
    if choice == 3:
        theword = random.choice(list3)
    return theword

while Game:
    os.system('cls')
    print("|***************************************|")
    print("|         Guess The Animal!!!           |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("| 1. Animals                            |")
    print("| 2. Fruits                             |")
    print("| 3. colors                             |")
    print("|First we will provide you with one hint|")
    print("|           !Your Hint Is!              |")
    print("|  These animals are big fans of water  |")
    print("|***************************************|")

    
    print(name, end = ", ")
    answer = input("would you like to play the game? ")
    answer = answer.lower()
    if 'n' in answer:
        Game = False
        break

    while True:
        choice = input("What game would you like to play 1,2, or 3? ")
        try:
            choice = int(choice)
            if choice > 0 and choice < 4:
                break
            else:
                print("give me 1,2, or 3")
        except:
            print("Plese enter a number")

    os.system('cls')

    theWord = selectWord(choice)

    check = True
    while check and count <5:
        guess=input("plese put your guess here: ")
        if guess == theword:
            print("Congrats, You got it")
            check = False
        else:
            hint()
        count += 1
        if count == 5:
            print("sorry you did not gess the word correctly")
    score = 200-40*(count-1)
    if score > high:
        high = score
    print(name + ", your score is " + str(score))
    input("Plese press enter ")

    os.system('cls')
    answer = input("Do you want to play again? ")
    if ('n' or 'N') in answer:
        Game = False
        print("Thank you for playing")

print("Your highest score is " + str(high))
#update file below

date = datetime.datetime.now()
scrLine = str(score)+"\t"+name+"\t"+date.strftime("%m-%d-%y")+"\n"
myFile = open("Danialhighscore", 'a')
myFile.write(scrLine)
myFile.close

myFile = open("Danialhighscore", 'r')
stuff=myFile.readlines()
myFile.close()
for line in stuff:
    print(line)
