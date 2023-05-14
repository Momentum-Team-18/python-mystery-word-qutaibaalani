import random


# This function is to open and to read the file
def open_file(file):
    # To open the file in read mode
    with open(file) as my_file:
        # To make the file readable
        data = my_file.read()
        # To put the words into a list
        format_data = data.split()
        # To catch the formatted data
        return format_data


# This function is to chose the random word
def random_word(lst):
    # To select the random word from the blank list
    word = random.choice(lst)
    # To catch the random word
    return word


def play_game():
    # Select a random word from the file "words.txt"
    chosen_word = random_word(open_file("words.txt"))
    # Determine the length of the chosen word
    word_length = len(chosen_word)
    # Create a list of underscores representing each letter in the word
    underscore = ["_ "] * word_length

    # Print the chosen word (for debugging purposes)
    print(chosen_word)
    # Print the number of letters in the chosen word
    print(f"Your word has {word_length} letters.")
    # Print the underscores representing the unguessed letters of the word
    print("".join(underscore))

    # Initialize an empty list to store the guesses made by the player
    guesses = []
    # Initialize the guess count to 0
    guess_count = 0


if __name__ == "__main__":
    play_game()
