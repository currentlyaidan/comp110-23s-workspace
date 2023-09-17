"""EX02 - One Shot Wordle"""

__author__: str = 730679404

secret_word: str = "python"
word_guess: str = input("What is your 6-letter guess? ")
index_number: int = 0
printed_string: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
found_letter: bool = False
check_all: int = 0

while len(word_guess) != 6:
    word_guess = input("That was not 6 letters! Try again: ")

while index_number < len(word_guess):
    check_all = 0
    if word_guess[index_number] == secret_word[index_number]:
        printed_string += (GREEN_BOX)
        index_number += 1
    else:
        while not(found_letter == False) and (check_all < len(word_guess)):
            if secret_word[check_all] == word_guess[index_number]:
                found_letter = True
            else:
                check_all += 1
    if (found_letter == True):
        printed_string += (YELLOW_BOX)
        index_number += 1
    else:
        printed_string += (WHITE_BOX)
        index_number += 1

if word_guess == secret_word:
    print(printed_string)
    print("Woo! You got it!")
else:
    print(printed_string)
    print("Not quite. Play again soon!")