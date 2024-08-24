import random as rand
import guess_data as gs

playAgain = True
default_value = False
#  0
# /|\
# /'\

def play_again():
    global playAgain

    print("Do you wish to play again?")
    answer = input().lower()

    while answer != "yes" and answer != "no":
        print("Please enter yes or no.")
        answer = input().lower()

    if answer == "yes":
        playAgain = True
        gs.checked_letters = {key: default for key in gs.checked_letters} # resetting the dictionary
    elif answer == "no":
        print("Thanks for playing!")
        playAgain = False

while playAgain == True:
    print("Guess the word!")
    word = rand.choice(gs.words)
    mistakes = 0
    check = ["_" if letter != " " else " " for letter in word]
    print(" ".join(check)) # displays check with a " " between each element

    word_guessed = False
    while word_guessed == False and mistakes < 7:
        answer = input("What letter are you choosing? ").lower()

        if answer == word.lower():
            word_guessed = True
            break

        if answer not in gs.checked_letters and ((not answer.isalpha()) or (answer.isalpha() and len(answer) != 1)):
            print("Please enter a letter! " )
            continue

        if answer not in word.lower():
            if gs.checked_letters[answer] == False:
                gs.checked_letters[answer] = True
                print("Sorry, that's not in the word!")
                print(gs.messages[mistakes])
                print(gs.hang_man[mistakes])
                mistakes += 1
                print()
            else:
                print("You've already guessed that letter!")
        else:
            if gs.checked_letters[answer] == False:
                gs.checked_letters[answer] = True
                for index, letter in enumerate(word):
                    if letter.lower() == answer:
                        check[index] = letter
                for letter in check:
                    print(letter, end=' ')
                if "_" not in check:
                    word_guessed = True
                print()
            else:
                print("You've already guessed that letter!")
    if word_guessed:
        print("You guessed the word!")
        print(f"The word was {word}.")
    else:
        print("You didn't guess the word!")
        print(f"The word was {word}.")
    play_again()
