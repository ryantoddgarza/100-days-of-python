#!/usr/bin/env python3
"""Random password generator."""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters= int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

pwd_list = []
password = ""

for n in range(0, n_letters):
    pwd_list.append(random.choice(letters))

for n in range(0, n_symbols):
    pwd_list.append(random.choice(symbols))

for n in range(0, n_numbers):
    pwd_list.append(random.choice(numbers))

random.shuffle(pwd_list)

for char in pwd_list:
    password += char

print(f"Your password is: {password}")
