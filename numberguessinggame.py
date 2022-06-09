#Aidan Zrski
#Pseudocode
#
import os
os.system('cls')
import random
import datetime

def print_instructions(): # this function prints the instructions
    Myfile = open("numberguessinstructions.txt", "r")
    stuff = Myfile.readlines()
    Myfile.close()
    for line in stuff:
        print(line)

def createguesssinggame(range, tries): # this function creates the guessing game
    random_number = random.randint(1, range)
    x = 0
    score = 0
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
            score = 40*(tries+1 - x)
            print("your score is "+str(score)) 
            break
        if x == tries and player_guess != random_number:
            print("you lost stupid this is an easy game")
            break
        if player_guess != random_number:
            if player_guess > random_number:
                print("your guess was high")
                print("you have " + str(tries-x) + " tries left")  
            else:
                print("your guess was low")    
                print("you have " + str(tries-x) + " tries left")            
    return score  


def scoreboard(): # this function displays the top 5 scores
    myFile = open("numberscore.txt","r")
    stuff = myFile.readlines()
    stuff.sort(reverse=True)
    myFile.close()
    x=1
    for line in stuff:
        print(line)  
        x+=1
        if x == 5:
            break



name = input("enter a name: ") # gets the users name
Game=True
score = 0
while Game: # creates a loop for the game

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



    while True: # makes sure the player inputs the correct value
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
        os.system('cls')
        print_instructions() # prints the instructions
    if choice == 2:
        os.system('cls')
        score = createguesssinggame(25, 6) # creates the guessing game with a range of 25 and 6 tries
    if choice == 3:
        os.system('cls')
        score = createguesssinggame(50, 8) # creates the guessing game with a range of 50 and 8 tries
    if choice == 4:
        os.system('cls')
        score = createguesssinggame(100, 10) # creates the guessing game with a range of 100 and 10 tries
    if choice == 5:
        os.system('cls')
        scoreboard()   # displays the scoreboard
    if choice == 6:
        os.system('cls')
        Game = False   # ends the game

date = datetime.datetime.now()
scrLile=str(score)+"\t"+date.strftime('%m / %d/ %y')+"\t"+name +"\n"
myFile=open("numberscore.txt", 'a') 
myFile.write(scrLile) # adds the score to the game
myFile.close()             