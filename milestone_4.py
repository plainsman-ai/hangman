import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # a list of the possible words
        self.word_list = word_list or []
        # the number of lives the player starts with.
        self.num_lives = num_lives
        # the word to be guessed
        self.word = random.choice(word_list).lower()
        # list of backspace strings symbolising empty letters
        self.word_guessed = list("_" for letter in range(len(self.word)))
        # the number or unique letters in the word which haven't been guessed
        self.num_letters = {letter for letter in self.word}
        # list of letters which have already been guessed, starting with 0
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            guess = guess.lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


test_hangman = Hangman(["Apple", "Strawberry"])
test_hangman.ask_for_input()