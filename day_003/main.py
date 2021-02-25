#!/usr/bin/env python3
"""A choose your own adventure game."""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn_query = 'You\'re at a cross road. Where do you want to go? Type "left" or "right"?\n'
lake_query = 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
door_query = 'You arrive at the island unharmed. There is a house with three doors. One red, one yellow, and one blue. Which color do you choose?\n'

turn = input(turn_query).lower()

if turn == "left":
    lake = input(lake_query).lower()

    if lake == "wait":
        door = input(door_query).lower()

        if door == "yellow":
            print("You win!")
        elif door == "red":
            print("You were burned by fire.\nGame over!")
        elif door == "blue":
            print("You were eaten by beasts.\nGame over!")
        else:
            print("You chose a door that doesn't exist. Game over!")
    else:
        print("You were attacked by a giant trout.\nGame over!")
else:
    print("You fell into a hole.\nGame over!")
