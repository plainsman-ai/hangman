import random

word_list = ["Mango", "Strawberry", "Peach", "Pumpkin", "Chocolate"]
print(word_list)

word = random.choice(word_list)

guess = input("Please enter a single letter:")

if len(guess) == 1 and guess in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
    print("Good Guess!")
else:
    print("Ooops! That is not a valid input.")
print(word)

