"""EX01 - A cute step towards Wordle."""

__author__ = "730679404"

five_letter_word: str = input("Enter a 5 character word: ")
single_character: str = input("Enter a single character: ")

print("Searching for " + str(single_character) + " in " + str(five_letter_word))
if single_character == five_letter_word[0]:
    print(str(single_character) + " found at index 0")
if single_character == five_letter_word[1]:
    print(str(single_character) + " found at index 1")
if single_character == five_letter_word[2]:
    print(str(single_character) + " found at index 2")
if single_character == five_letter_word[3]:
    print(str(single_character) + " found at index 3")
if single_character == five_letter_word[4]:
    print(str(single_character) + " found at index 4")
