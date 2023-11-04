# Step 1: Randomly choose a word from the word_list and assign it to a variable called chosen_word
# Step 2: Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Step 3: Check if the letter the user guessed (guess) is one of the letters in the chosen_word


import random

def randomWord():
    words = ["Apple", "Banana", "Mouse", "Horse", "Python", "AWS", "Javascript", "Hindi"]
    choosen_word = random.choice(words)
    return choosen_word.lower()


def handman(life):
    if life == 5:
        print("O")
    elif life == 4:
        print(" O ")
        print("/")
    elif life == 3:
        print(" O ")
        print("/|")
    elif life == 2:
        print(" O ")
        print("/|\\")
    elif life == 1:
        print(" O ")
        print("/|\\")
        print("/")
    else:
        print(" O ")
        print("/|\\")
        print("/ \\")
        return True
    return False


def replaceChar(dashed_string, char, idx):
    dash_list = list(dashed_string)
    dash_list[idx] = char
    return ''.join(dash_list)


def playGame(choosen_word, dashed_string, life):
    while(life):
        char = input("Guess a character: ").lower()
        if char in choosen_word:
            for idx, letter in enumerate(chosen_word):
                if letter == char:
                    dashed_string = replaceChar(dashed_string, char, idx)
            print(dashed_string)

            if "_" not in dashed_string:
                print("You Win")
                return
        else:
            life-=1
            game_over = handman(life)
            if game_over:
                print("Game Over")
                return


if "__main__" == __name__:
    life = 6
    chosen_word = randomWord()      # Get Random Word
    dashed_string = ""
    for i in range(len(chosen_word)):
        dashed_string += "_"

    print(chosen_word)
    playGame(chosen_word, dashed_string, life)