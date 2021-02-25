#!/usr/bin/env python3
"""Rock, paper, scissors game."""

import random
import ascii_art

art_list = [ascii_art.rock, ascii_art.paper, ascii_art.scissors]
usr_query_string = "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"
usr_throw = int(input(usr_query_string))
computer_throw = random.randint(0, 2)

if usr_throw > 2:
    print("You typed an invalid number. You lose.")
else:
    print(art_list[usr_throw])
    print("Computer chose:")
    print(art_list[computer_throw])

    if usr_throw == computer_throw:
        print("Tie")
    elif usr_throw == 0 and computer_throw == 1:
        print("You lose")
    elif usr_throw == 0 and computer_throw == 2:
        print("You win")
    elif usr_throw == 1 and computer_throw == 0:
        print("You win")
    elif usr_throw == 1 and computer_throw == 2:
        print("You lose")
    elif usr_throw == 2 and computer_throw == 0:
        print("You lose")
    elif usr_throw == 2 and computer_throw == 1:
        print("You win")
