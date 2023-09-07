"""EX01 - A cute step towards Wordle."""

__author__ = "730679404"

five_letter_word: str = input("Enter a 5 character word: ")
if len(five_letter_word) == 5:
    

single_character: str = input("Enter a single character: ")
matching_letters: int = 0

print("Searching for " + str(single_character) + " in " + str(five_letter_word))
if single_character == five_letter_word[0]:
    print(str(single_character) + " found at index 0")
    matching_letters += 1
if single_character == five_letter_word[1]:
    print(str(single_character) + " found at index 1")
    matching_letters += 1
if single_character == five_letter_word[2]:
    print(str(single_character) + " found at index 2")
    matching_letters += 1
if single_character == five_letter_word[3]:
    print(str(single_character) + " found at index 3")
    matching_letters += 1
if single_character == five_letter_word[4]:
    print(str(single_character) + " found at index 4")
    matching_letters += 1

if matching_letters == 0:
    print("No instances of " + str(single_character) + " found in " + str(five_letter_word))
if matching_letters == 1:
    print(str(matching_letters) + " instance of " + str(single_character) + " found in " + str(five_letter_word))
if matching_letters > 1:
    print(str(matching_letters) + " instances of " + str(single_character) + " found in " + str(five_letter_word))