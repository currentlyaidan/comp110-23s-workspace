"""Program that loops until correct number is guessed"""

from random import randint

secret: int = randint(1,10)
guess: int = int(input("Guess a number between 1 and 10: "))
number_of_tries: int = 0
max_tries: int = 3


while (guess != secret) and (number_of_tries < (max_tries - 1)):
    print("Wrong")
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10!")
    # If guess is too low, tell them
    if guess < secret:
        print("Too low!")
    # If guess is too high, tell them
    elif guess > secret:
        print("Too high!")
    # Ask for a different guess
    print(f"You have {(max_tries - 1) - number_of_tries} tries left")
    guess = int(input("Guess again: "))
    number_of_tries += 1
# If I've reached this point, guess == secret
if guess == secret:
    print("You guessed correctly!")
else:
    print("You lose. :(")
