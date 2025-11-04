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
#Removed the Sleep import from original as not essential.

alphabet = string.ascii_lowercase  #"abcdefghijklmnopqrstuvwxyz"

# updated code that Encrypts or decrypts a message using Caesar cipher.
def caesar_cipher(message, key, decrypt=False):
    answer = ""

    for c in message:
        if c.lower() in alphabet: #This will handle both uppercase and lowercase
            position = alphabet.find(c.lower()) #.lower() returns a string where all characters are lower case

           #Adding a new encryption feature (very similar structure to decrypting)
            if decrypt:
                new_position = (position - key) % 26
            else:
                new_position = (position + key) % 26
                #this will make it so the word shifts left if decrypting, and right if encrypting
            new_character = alphabet[new_position]
            # Function to preserve original case
            if c.isupper():
                answer += new_character.upper()
            elif c.islower():
                answer += new_character.lower()
            else:
                answer += c

            return answer


    #print("\nDecrypting your message...\n")
    #sleep(2)  # give an appearance of doing something complicated
    #print("Stand by, almost finished...\n")
    #sleep(2)  # more of the same
    #print("Your decrypted message is:\n")
    #print(message)
