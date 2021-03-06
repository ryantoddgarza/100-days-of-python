#!/usr/bin/env python3
"""Caesar cipher."""

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(string, n_shift, direc):
    output = ""

    if direc == "decode":
        n_shift *= -1

    for char in string:
        if char in alphabet:
            shifted_index = alphabet.index(char) + n_shift
            wrapped_index = shifted_index % len(alphabet)
            output += alphabet[wrapped_index]
        else:
            output += char

    print(f"The {direc}d text is: {output}")

PROGRAM_RUNNING = True
print(logo)

while PROGRAM_RUNNING:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(text, shift, direction)

    run_again = input("Cipher another string? (yes/no)\n").lower()

    if run_again != "yes":
        PROGRAM_RUNNING = False
        print("Goodbye")
