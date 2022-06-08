#Aidan Zrski
#Pseudocode
#
import os
os.system('cls')
import random

def print_instructions(): # this function prints the instructions
    Myfile = open("numberguessinstructions.txt", "r")
    stuff = Myfile.readlines()
    Myfile.close()
    for line in stuff:
        print(line)

def createguesssinggame(range, tries, scremax): # this function create the guessing game
    random_number = random.randint(1, range)
    x = 0
    while x < tries: 
        x +=1       
        while True:
            player_guess = input("Enter a number between 1 and "+str(range)+": ")
            try:
                player_guess = int(player_guess)
                if player_guess > 0 and player_guess < range+1:
                    break
                else:
                    print("give me a number in range 1 - "+str(range))
            except:
                print("Plese enter a number")
        if player_guess == random_number:
            print("you guessed the number in "+str(x)+" tries") 
            break
        if player_guess != random_number:
            if player_guess > random_number:
                print("your guess was high")
                print("you have " + str(tries-x) + " tries left")  
            else:
                print("your guess was low")    
                print("you have " + str(tries-x) + " tries left")         


# createguesssinggame(25, 4, 160)


    

# createguesssinggame()

# print_instructions()

Game=True
while Game:
    os.system('cls')
    print("|***************************************|")
    print("|         Guess a number!!!             |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("| 1. Print instructions                 |")
    print("| 2. guess a number 1 - 25              |")
    print("| 3. guess a number 1 - 50              |")
    print("| 4. guess a number 1 - 100             |")
    print("| 5. print score                        |")
    print("| 6. exit                               |")
    print("|***************************************|")    



    while True:
        choice = input("Choose 1, 2, 3, 4, 5, or 6: ")
        try:
            choice = int(choice)
            if choice > 0 and choice < 7:
                break
            else:
                print("give me 1 - 7")
        except:
            print("Plese enter a number")

    if choice == 1:
        print_instructions()
    if choice == 2:
        createguesssinggame(25, 6, 240)
    if choice == 3:
        createguesssinggame(50, 8, 320)  
    if choice == 4:
        createguesssinggame(100, 12, 480)   
    if choice == 5:
        print("print the score")   
    if choice == 6:
        game = False        