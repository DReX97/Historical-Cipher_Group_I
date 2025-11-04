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
alphabet = string.ascii_lowercase + string.digits  # letters from a-z an num 0-10
#Removed the Sleep import from original as not essential.
class CaesarCipher:
    def __init__(self):
        print("\nWelcome to the Caesar Cipher. ")

# updated code that Encrypts or decrypts a message using Caesar cipher.
    def caesar_cipher(self,message, key, decrypt=False):
        answer = ""
        length = len(alphabet)

        for c in message:
            if c.lower() in alphabet: #This will handle both uppercase and lowercase
                position = alphabet.find(c.lower()) #.lower() returns a string where all characters are lower case

               #Adding a new encryption feature (very similar structure to decrypting)
                if decrypt:
                    new_position = (position - key) % length
                else:
                    new_position = (position + key) % length
                    #this will make it so the word shifts left if decrypting, and right if encrypting
                new_character = alphabet[new_position]
                # Function to preserve original case
                if c.isupper():
                    answer += new_character.upper()
                else:
                    answer += new_character
            else:
                answer += c

        return answer

    def get_key(self):
            #this will ask the user for a key to shift the word
            while True:
                try: #ask for user to enter a should be a number between 0 and 26
                    key = int(input("Please enter a key: "))
                    if 0 <= key <= 26:
                        return key
                    else: #in case user enters an invalid number
                        print("Please enter a valid key (0/26)")
                except ValueError: #incase user enters a character
                    print("Please enter a number, not text.")

#menu screen for the Caesar
    def c_menu(self):

        while True:
            # This Lets the user choose whether they want to encrypt or decrypt a message
            print("\nDo you want to:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            print("3. Return to Cipher selection")

            choice = input("Enter choice (1/2/3): ").strip() #.strip just removes the spaces at the beginning and the end

#if 1 is entered, prompts user for a message to encrypt
            if choice == "1":
                message = input("Enter message to encrypt: ").strip()
                key = self.get_key()
                #result combines chosen message and key to encrypt using caesar
                result = self.caesar_cipher(message, key)
                print(f"Encrypted message: {result}")

#if 2 entered, prompts user for a message to decrypt
            elif choice == "2":
                message = input("Enter message to decrypt: ").strip()
                key = self.get_key()
                result = self.caesar_cipher(message, key, decrypt=True) #tells the method to decrypt instead of encrypt
                print(f"Decrypted message: {result}")

            elif choice == "3":
                print("Returned to Cipher Selection")
                break


if __name__ == "__main__":
    CaesarCipher().c_menu()
