"""EX03 - Stuctured Wordle."""

__author__ = "730679404"


def contains_char(secret_word: str, chr_guess: str) -> bool:
    """Function searches the word for the guessed character, returns true if found and false if not."""
    assert len(chr_guess) == 1
    check_chr: int = 0
    while check_chr < len(secret_word):
        # Check if the character is the same
        if secret_word[check_chr] == chr_guess:
            return True
        # If not, then add one and check the next character
        else:
            check_chr += 1
    return False


def emojified(guess_word: str, secret_word: str) -> str:
    """Function checks all characters and assigns a proper emoji."""
    # Establish all variables
    assert len(guess_word) == len(secret_word)
    check_chr: int = 0
    emojified_string: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while check_chr < len(guess_word):
        # Check the character
        if secret_word[check_chr] == guess_word[check_chr]:
            # Concantenate a green box
            emojified_string += GREEN_BOX
            check_chr += 1
        else: 
            if contains_char(secret_word, guess_word[check_chr]) is True:
                # Concatenate a yellow box
                emojified_string += YELLOW_BOX
                check_chr += 1
            else:
                # Concatenate a white box
                emojified_string += WHITE_BOX
                check_chr += 1 
    return emojified_string


def input_guess(valid_length: int) -> str:
    """Function prompts user for a valid input until given."""
    # Have the user input a word
    user_response: str = input(f"Enter a {valid_length} character word: ")
    while len(user_response) >= 0:
        # If correct, output the valid word
        if len(user_response) == valid_length:
            return user_response
        # Have them try again until a valid response is given
        else:
            user_response = input(f"That wasn't {valid_length} chars: Try again: ")
    return user_response


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Establish all variables
    turns_left: int = 1
    secret_word: str = "codes"
    user_guess: str = ""

    while turns_left <= 6:
        user_guess = input_guess(len(secret_word))
        print(f" === Turn {turns_left}/6 ===")
        print(emojified(user_guess, secret_word))
        # If correct, end the program
        if user_guess == secret_word:
            print(f"You won in {turns_left}/6 turns!")
            turns_left = 7
        # Otherwise, try again
        else:
            turns_left += 1
    # When you're out of turns, check to see if you've lost.
    if user_guess != secret_word:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()