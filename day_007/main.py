#!/usr/bin/env python3
"""Hangman game."""

import random
from os import system
from dictionary import words
from ascii_art import logo, stages

GAME_OVER = False
LIVES = len(stages) - 1
chosen_word = random.choice(words)
guess_list = []

display = []
for n in range(len(chosen_word)):
    display.append("_")

print(logo)

while not GAME_OVER:
    guess = input("Guess a letter: ").lower()
    system('clear')

    for i,char in enumerate(chosen_word):
        if char == guess:
            display[i] = char

    if guess in guess_list:
        print(f"You've already guessed the letter {guess}.")
    else:
        if guess not in chosen_word:
            print(f"the letter {guess} is not in the word.")
            LIVES -= 1
            if LIVES == 0:
                GAME_OVER = True
                print(f"You lose.\nThe solution was {chosen_word}")

        guess_list.append(guess)

    print(f'{" ".join(display)}')
    print(stages[LIVES])

    if "_" not in display:
        GAME_OVER = True
        print("You win!")
