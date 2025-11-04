"""
link to original source: https://gist.github.com/AO8/3a89ba7c8f032c7a1ff505baa3ce970e
This Python Script was written by the creator under the handle A08. In the Gist, he has added a simple version
of caesar cipher using python with only the decryption function that is not fully complete.
My contribution will be to add the choice for the user to choose a type of cipher they want,
Add an encryption mode that will allow the user to create their own caesar,
Let the user choose after selecting caesar, whether they want to encrypt or decrypt a message,
Allow for the word to be Case sensitive and numbers allowed.
"""

import string
from time import sleep

alphabet = string.ascii_lowercase  #"abcdefghijklmnopqrstuvwxyz"


def decrypt():
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))

    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("\nDecrypting your message...\n")
    sleep(2)  # give an appearance of doing something complicated
    print("Stand by, almost finished...\n")
    sleep(2)  # more of the same
    print("Your decrypted message is:\n")
    print(decrypted_message)


decrypt()