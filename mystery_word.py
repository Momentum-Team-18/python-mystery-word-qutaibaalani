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
def random_word(list):
    # To select the random word from the blank list
    word = random.choice(list)
    # To catch the random word
    return word


print(word)


def play_game():
    pass


if __name__ == "__main__":
    play_game()
