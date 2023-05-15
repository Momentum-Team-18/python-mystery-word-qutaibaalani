# Word Guessing Game

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


# This function is to choose a random word
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

    # Loop until the number of guesses reaches 8
    while guess_count < 8:
        # Prompt the user to enter a letter
        user_guess = input("Guess a letter: ")
        # Print the user's guess
        print("Guess:", user_guess)

        # Check if the input is longer than a single character
        if len(user_guess) > 1:
            # Print a message indicating an invalid guess
            print("Try again")
            # Check if the guess is incorrect and not previously made
        elif user_guess not in chosen_word and user_guess not in guesses:
            # Increment the guess count
            guess_count += 1
            # Add the incorrect guess to the list
            guesses.append(user_guess)
            # Print the updated guess count
            print("Wrong guesses:", guess_count)
            # Print the incorrect guesses so far
            print("Guesses:", guesses)
            # Check if the guess is correct
        elif user_guess in chosen_word:
            # Iterate over the letters in the chosen word
            for letter in range(len(chosen_word)):
                # Check if the guessed letter matches a letter in the chosen word
                if user_guess == chosen_word[letter]:
                    # Replace the underscore with the correct letter
                    underscore[letter] = chosen_word[letter]
                    # Add the correct guess to the list
                    guesses.append(user_guess)
            # Print the updated word with revealed letters
            print("".join(underscore))
            # Check if all the underscores have been replaced (word fully guessed)
            if "_ " not in underscore:
                # Print a winning message
                print("WooHoo! You've Got It! Congratulations!")
                # Ask the user if they want to play again
                play_again = input("Do you want to play again? (Y/N) ")
                # If the user wants to play again
                if play_again.lower() == "y":
                    # Restart the game
                    play_game()
                # Exit the program
                else:
                    exit()

    else:
        # Print the chosen word when the number of guesses reaches 8
        print("The word was:", chosen_word)
        # Ask the user if they want to play again
        play_again = input("Game Over. Would you like to try again? (Y/N) ")
        # If the user wants to play again
        if play_again.lower() == "y":
            # Restart the game
            play_game()
        else:
            # Exit the program
            exit()


# Start the game when the script is run directly
if __name__ == "__main__":
    play_game()
