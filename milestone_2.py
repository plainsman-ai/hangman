import random

# Describes a list of fruit and chooses one at random.

word_list = ["Mango", "Strawberry", "Peach", "Pumpkin", "Chocolate"]

print(word_list)

word = random.choice(word_list)

# Asks user to input a letter and tells them if valid choice.

guess = input("Please enter a single letter:")

if len(guess) == 1 and guess in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
    print("Good Guess!")
else:
    print("Ooops! That is not a valid input.")

# Print random choice of fruit from earlier.

print(word)

