import random

target = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess: "))

    if guess > target:
        print("Too high")
    elif guess < target:
        print("Too low")
    else:
        print("Correct!")
        break