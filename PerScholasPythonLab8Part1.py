#Working with Loops
import random

#Describes the Game
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

#Generates random number
number = random.randint(1,10)

#Make value for guesses
isGuessRight = False

#While loop for game
while isGuessRight != True:
    #user enters guess
    guess = input("Guess a number between 1 and 10: ")
    #if user enters correctly
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
   #if user enters incorrectly
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))