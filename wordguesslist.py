import random
# Aidan Zarski

# Psudocode
# 

import os
os.system('cls')

# instructions
print("guess a word")
print("if you guess the word wrong thats ok because you have unlimited tries, but your tries will be counted")
print("if you want the first letter(s) in the word type hint, but this will count as a try. You only get 3 hints")
print("if you want to give up just type quit")


fruit_words = ["apple", "berry", "cherry", "strawberry", "watermelon", "pineapple", "lemon", "grape", "bannana", "grapefruit"] # the ten words

run = True
while run: # allowes the player to play the guessing game multipe times



    random_fruit = random.choice(fruit_words) # randomly picks a word from my words
    word_pick = "" 
    tries = 0 # how many tries the player used
    hints = 0 # how many hints the player used

    while random_fruit != word_pick:
        word_pick = input("type a fruit: ")
        tries += 1 # adds 1 to the tries count
        if word_pick != random_fruit and word_pick != "quit" and word_pick != "hint":
            print("you got it wrong, you used",tries,"tries so far")
        if word_pick == "quit": # if the player types quit the games over
            break
        if word_pick == "hint" and hints == 3: # if the player is out of hints this code runs
            print("you are out of hints, the first three letters are "+ random_fruit[0:hints])  
            tries -= 1  
        if word_pick == "hint" and hints < 3: # if the player still has hints left this code runs
            hints += 1
            print("the word starts with the letter(s) " + random_fruit[0:hints])



    if random_fruit == word_pick:
        print("You quessed the word in",tries,"tries!")
    else:
        print("you gave up ):") 

    play_again = input("do you want to play again? if you dont type no, otherwise press enter ") # if the player types no the program ends
    if play_again == "no":
        run = False       