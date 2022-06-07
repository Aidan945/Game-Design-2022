import random
# Aidan Zarski

# Psudocode
# Input a fruit
# use random.choice to sellect a random fruit from the list
# if the player guesses the correct fruit give them the option to play agin
# if the player guesses the fruit wrong let them try again
# if the player types hint give them a letter in the word
# if a player types quit end the guessing game
# after the guessing game the player has an option to play again and they type yes or no
# The players tries and hints are counted, the player has unlimited tries but only 3 hints

import os
os.system('cls')





run = True
while run: # allowes the player to play the guessing game multipe times

    # instructions
    print("guess a word")
    print("if you guess the word wrong thats ok because you have unlimited tries, but your tries will be counted")
    print("if you want the first letter(s) in the word type hint, but this will count as a try. You only get 3 hints")
    print("if you want to give up just type quit")
    print(" ")

    fruit_words = ["apple", "berry", "cherry", "strawberry", "watermelon", "pineapple", "lemon", "grape", "bannana", "grapefruit"] # the ten words
    computer_parts = ["CPU", "GPU", "Power supply", "RAM", "Heat sink", "motherboard", "coolant", "water cooled", "SSD", "hard drive"]
    Games = ["Call of duty", "Fortnite", "Minecraft", "Plants vs Zombies", "Bloons Tower Defence", "Clash Royale", "Clash of Clans", "Stumble Guys", "Ratchet and Clank", "Miles Morales"]
    
    check = True
    while check:
        try:    
            list_pick = int(input("Enter 1 to guess fruits, 2 to guess computer parts, or 3 to guess games."))
            if list_pick > 0 and list_pick < 4:
                check = False
            else:
                print("only enter 1, 2, or 3")
        except ValueError:
            print("Please enter a number")
        
    if list_pick  == 1:
        list = fruit_words
        list_word = "fruit"
    if list_pick == 2:
        list = computer_parts
        list_word = "computer part"
    if list_pick == 3:
        list = Games
        list_word = "game"


    random_word = random.choice(list) # randomly picks a word from my words
    word_pick = "" 
    tries = 0 # how many tries the player used
    hints = 0 # how many hints the player used

    while random_word != word_pick:
        word_pick = input("type a "+list_word+": ")
        tries += 1 # adds 1 to the tries count
        if word_pick != random_word and word_pick != "quit" and word_pick != "hint":
            print("you got it wrong, you used",tries,"tries so far")
        if word_pick == "quit": # if the player types quit the games over
            break
        if word_pick == "hint" and hints == 3: # if the player is out of hints this code runs
            print("you are out of hints, the first three letters are "+ random_word[0:hints])  
            tries -= 1  
        if word_pick == "hint" and hints < 3: # if the player still has hints left this code runs
            hints += 1
            print("the word starts with the letter(s) " + random_word[0:hints])



    if random_word == word_pick:
        print("You guessed the word in",tries,"tries!")
    else:
        print("you gave up ):") 

    play_again = input("do you want to play again? if you dont type no, otherwise press enter ") # if the player types no the program ends
    if play_again == "no":
        run = False       