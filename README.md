# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
## As of Milestone 3
The file milestone_3 returns a list of 5 pre-selected fruit and chooses one from random. 
It asks the user to guess a letter and tells them whether this is in the name of the fruit or not (it is not case-sensitive).
Each time it selects a different kind of fruit. This will be changed.

## As of Milestone 4
The file milestone_4 defines a Hangman class with two methods and an initializer.

The function initializes with a list of words and a number of lives. It chooses a word from the list at random and passes it to the two methods.

One of these methods runs indefinitely (needs to be modified) and asks the user to guess the letters in the word. This calls the other method, which checks whether the choice is valid.

The program runs indefinitely, even if every possible letter has been entered.