import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # a list of the possible words
        self.word_list = word_list or []
        # the number of lives the player starts with.
        self.num_lives = num_lives
        # the word to be guessed
        self.word = random.choice(word_list)
        # list of backspace strings symbolising empty letters
        self.word_guessed = list("_" for letter in range(len(self.word)))
        # the number or unique letters in the word which haven't been guessed
        self.num_letters = [letter for letter in self.word]
        # list of letters which have already been guessed, starting with 0
        self.list_of_guesses = []
    
test_hangman = Hangman(["Apple", "Strawberry"])
print(test_hangman.word_list)
print(test_hangman.num_lives)
print(test_hangman.word_guessed)