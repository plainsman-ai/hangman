import random

word_list = ["Mango", "Strawberry", "Peach", "Pumpkin", "Chocolate"]

word = random.choice(word_list)

def check_guess(guess):
    lower_guess = guess.lower()
    lower_word = word.lower()
    if lower_guess in lower_word:
        print(f"Good guess! {lower_guess} is in the word")
    else:
        print(f"Sorry, {lower_guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            print("Invalid letter. Please enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
