import random

class Hangman:
    def __init__(self, word_list, num_lives):
        # a list of the possible words
        self.word_list = word_list
        # the number of lives the player starts with.
        self.num_lives = num_lives
        # the word to be guessed
        self.word = random.choice(word_list).lower()
        # list of backspace strings symbolising empty letters
        self.word_guessed = list("_" for letter in range(len(self.word)))
        # the number of unique letters in the word which haven't been guessed
        self.num_letters = len({letter for letter in self.word})
        # list of letters which have already been guessed, starting with 0
        self.list_of_guesses = []
    
    """
    checks whether the guess applies to the word
    subtracts from lives if not, changes word_guessed if yes
    """
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            indexes = []
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word")
            print(f"You have {self.num_lives} left.")

        # below here are tests for designer
        # print(self.num_letters)
        # print(self.num_lives)


    """
    this method does the job. bosh
    previously had a while loop which never breaked
    """
    def ask_for_input(self):
        guess = input("Guess a letter: ")
        guess = guess.lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")    
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

play_game(["Mango", "Strawberry", "Peach", "Pumpkin", "Chocolate"])