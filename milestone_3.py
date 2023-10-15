import random

word_list = ["Mango", "Strawberry", "Peach", "Pumpkin", "Chocolate"]

word = random.choice(word_list)
    
while True:
    guess = input("Guess a letter: ")
    if guess.isalpha() and len(guess) == 1:
        break
    else:
        print("Invalid letter. Please enter a single alphabetical character.")

if guess in word:
    print(f"Good guess! {guess} is in the word")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")