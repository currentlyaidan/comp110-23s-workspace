"""EX02 - One Shot Wordle"""

__author__: str = 730679404

#set all variables to initial values
secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
index_number: int = 0
printed_string: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
found_letter: bool = False
check_all: int = 0

#detect for improper inputs and prompt repeatedly until user inputs valid input
while len(word_guess) != len(secret_word):
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

#detect if the letter is the same in each index
while index_number < len(word_guess):
    found_letter = False
    check_all = 0
    #if the letter is the same print green
    if word_guess[index_number] == secret_word[index_number]:
        printed_string += (GREEN_BOX)
        index_number += 1
    else:
        #check if the letter exists anywhere in the word
        while not(found_letter == True) and (check_all < len(word_guess)):
            if secret_word[check_all] == word_guess[index_number]:
                found_letter = True
            else:
                check_all += 1
        #if the letter exists elsewhere in the word, print yellow
        if not(found_letter == False):
            printed_string += (YELLOW_BOX)
            index_number += 1
        #otherwise, print white
        else:
            printed_string += (WHITE_BOX)
            index_number += 1
            
#output final string of boxes, as well as a success or failure message
if word_guess == secret_word:
    print(printed_string)
    print("Woo! You got it!")
else:
    print(printed_string)
    print("Not quite. Play again soon!")