#Guess the Number Game

import random
target = random.randint(1, 100)
print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100. Try to guess it!")
while True:
    guess = input("Enter your guess (between 1 and 100) or type 'Q' to quit: ")
    if guess.upper() == "Q":
        print("Thanks for playing!")
        break
    guess = int(guess)
    if guess == target:
        print("Congratulations! You guessed the correct number:", target)
        break
    elif guess < target:
        print("Too low! Try again.")
    else:  
        print("Too high! Try again.")
        
print("Thanks for playing the Guess the Number Game!")
print("---game over---")