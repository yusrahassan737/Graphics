# Name: Yusra Hassan
# Date: October 30, 2020
# Class: ICS3U1-02
# Description : Only-input version
# Note: This version asks for the letter first, icicle hits are random and 20 is the goal

import random

# Variables
# Posibble words (35) # Credit: https://www.words-to-use.com/words/winter/ for most words
words = ["arctic", "barren", "blustery", "cozy", "crisp", "crystal", "dreary","enchanting", "extreme", "fog", "frost", "frigid", "glistening", "harsh", "holidays", "insolation", "icy", "joviality", "knitting", "leafless", "misty", "north", "numb", "opaline", "polar", "powdery", "quicksilver","recluse", "slippery", "snow", "toasty", "unending","vast", "windy", "zero"]

# Others
hits = 0
gameOver = False
lettersUsed = []
totalDisplayWords = 50


# Game loop (no pygame)
while gameOver != True:
    hitByIcicles = random.choice([True, False])
    
    # User's letter - includes error handling for an already used letter, an input that isn't a letter and more than one letter
    userLetter = input("Enter a letter: ")
    while userLetter in lettersUsed or len(userLetter) > 1 or userLetter.isalpha() != True:
        userLetter = input("Try again. Enter a letter: ")
    lettersUsed.append(userLetter)
    
    # Lets users choose how many words to play with each time. Error handling makes sure that the number of piles of 5 is from 1-3 and that it is less than the total amount of words allowed to use that are left for the round
    numDisplayWords = input("Enter how many (1, 2 or 3) rows of 5 words should be picked: ")
    while (numDisplayWords != "1" and numDisplayWords != "2" and numDisplayWords != "3" or int(numDisplayWords) * 5 > totalDisplayWords):
        numDisplayWords = input("Try again with a different number: ")
    numDisplayWords = int(numDisplayWords) * 5 # Total number of words
    totalDisplayWords -= numDisplayWords

    # Choose words to display using shuffle, so that there is only one of each. The number selected is the number of display words previously chosen
    random.shuffle(words)
    displayedWords = words[:numDisplayWords]
   
    # User gets a hit for however many times their letter showed up in all words from the word list, if they weren't blocked by icicles
    if hitByIcicles == False:
        for j in displayedWords:
            if userLetter in j:
                hits += j.count(userLetter)
    
    # Print user's hits and words
    print(displayedWords)
    if hitByIcicles:
        print("You were blocked by icicles. No hits this time.")
    else:
        print("You got %i hit(s)." %hits)
    
    # Win
    if (hits >= 20): # for now
        print("You won!")
        gameOver = True
    # Lose
    elif (totalDisplayWords == 0): 
        print("You lost :(")
        gameOver = True
