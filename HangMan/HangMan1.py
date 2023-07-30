import random

def get_random_word():
    word_list = ["apple", "banana", "orange", "grape", "watermelon", "pineapple", "strawberry", "mango", "cherry", "pear"]
    random_word = random.choice(word_list)
    return random_word

def print_underscores(word):
    underscores = '_' * len(word)
    print(underscores)


def check_letter(word):
    letter = input("guess a letter: ")

    if letter in word:
        return [i for i, char in enumerate(word) if char == letter]
        
    else:
        print(letter + " is not in the word")
        return []
    
def print_indexes_and_underscores(word, indices):
    for i in range(len(word)):
        if i in indices:
            print(word[i], end="")
        else:
            print("_", end="")
    print()


def start_game():
    # Add your Hangman game logic here
    print("Hangman game started!") 



    new_word = get_random_word()
    print(new_word)
    print_underscores(new_word)
    position = check_letter(new_word)
    print(position)
    print_indexes_and_underscores(new_word, position)
    
    





def play_hangman():
    while True:
        response = input("Do you want to play 'Hangman'? (y/n): ").lower()
        if response == 'y':
            start_game()
            break
        elif response == 'n':
            print("Terminating the program.")
            break
        else:
            print("Did not understand response, please select y or n")

if __name__ == "__main__":
    play_hangman()
