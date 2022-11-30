# Libraries
import random

# Getting words list and defining it
with open ('words.txt', 'r') as f:
    word_list = f.readlines()

# Game variables
completed = False
word = random.choice(word_list)[:-1]
attempts = 10
guesses = []

# Main Script
while not completed:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"You've {attempts} attempts remaining; guess a letter: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        attempts -= 1
        if attempts == 0:
            break

    completed = True
    for letter in word:
        if letter.lower() not in guesses:
            completed = False

if completed:
    print(f"Correct! The word was {word}, thanks for playing hangman!")
else:
    print(f"You have ran out of attempts, the word was: {word}")