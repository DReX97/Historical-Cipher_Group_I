"""
Original Source: https://github.com/ekcaroline/Classical-Ciphers-Railfence/blob/main/railfence_encrypt.py
Accessed: 30 Oct 2025
Modified by Damien Ho

Description:
This is the baseline Rail Fence Cipher implementation originally sourced from GitHub.
My Contribution includes:
-Implemented decryption function.
-Refactored the code into an object-oriented class structure (RailFenceCipher) for modular use.
-Removed spaces from input before encryption.
-Added error handling for invalid numeric inputs (try/except)
-Added input validation for empty messages and rail key limits
-Removed unnecessary 21-character restriction from original
-Improved user feedback and readability for better usability
-Enhanced user interface with better visual separators
-Added validation for Y/N grid input to prevent invalid responses
-Integrate with main.py for group project demo.
"""
import string


# =========================================================================
# Damien: Refactored Rail Fence Cipher into an object-oriented class for better modular integration
# =========================================================================
class RailFenceCipher:
    def __init__(self):#'self' represents the instance created when this class is called.
        print(
            "Welcome! This Python program takes a user-provided key and message, then encrypts the message using the Rail Fence Cipher. It creates a matrix to represent the zigzag pattern and fills it with the message's characters. The resulting matrix is printed, showing the encrypted message in a Rail Fence pattern. The program ensures user inputs meet the criteria for a valid encryption.\n"
        )
        print("Rail Fence Cipher module initialized. ")


    def railfence_encryption(self, rails, message):
        print("\nWe will now began to perform the railfence cipher. ")

        # =========================================================================
        #Damien: Improved encryption to ignore spaces before building the matrix
        message = message.replace(" ","")
        # =========================================================================

        # Create matrix
        fence = [[' ' for i in range(len(message))] for j in range(rails)]

        row, col = 0, 0
        rowmod = 1

        for i in range(len(message)):
            fence[row][col] = message[i]

            # Move to the next column and next row
            col += 1
            row += rowmod

            # If we reach the last row, reset to the first row and move to the next column
            if row == rails - 1:
                rowmod = -1
            elif row == 0:
                rowmod = 1

        encrypted_message = []

        # Puts the rows into a list
        for row in fence:
            encrypted_message.append(''.join(row))

        # formats the encrypted message
        format_enc_message = ""
        for i in encrypted_message:
            format_enc_message += i

        format_enc_message = format_enc_message.replace(" ", "")
        print("--------------------------------------------------------------------")
        print(f"\nEncrypted message: {format_enc_message}")
        print("\n--------------------------------------------------------------------")

        # =========================================================================
        #Damien: Added user input validation loop for grid display, ensuring user can only enter 'Y' or 'N' (prevents numbers or invalid input)
        while True:
            # Show grid
            userChoice = input("\nWould you like to see the grid? (Y/N) ")
            print("--------------------------------------------------------------------")
            if userChoice.lower() == "y":
                print("\n===>>> Rail Fence Grid <<<===")
                for row in fence:
                    print(''.join(row))
                break
            elif userChoice.lower() == "n":
                print("Okay, thank you for using the railfence cipher.")
                break
            else:
                print("Invalid Input! Please select a valid choice. ")
                print("\nPlease enter 'Y' or 'N'. ")
                continue

    #=========================================================================
    # Rail fence decryption function
    #Author: Damien Ho
    #Description:
    #           This function performs decryption for the Rail Fence Cipher.
    #           It reconstructs the zig zag pattern used during encryption,
    #           fills the matrix with ciphertext letters in the correct order,
    #           and then reads the message diagonally to reveal the plaintext.
    #=========================================================================
    def railfence_decryption(self, rails, cipher):#I renamed the variable in the parameter from user_message to cipher to make the code more semantically correct and easier to understand personally.
        print("\nWe will now began to perform the railfence cipher decryption. ")

        #Step 1: Create an empty 2D matrix (list of lists)
        #Each row represents a rail, and each column represents a letter position
        #Fill the matrix initially with '\n' to mark empty cells
        rail =[['\n' for i in range(len(cipher))] for j in range(rails)]

        #Step 2: Mark where characters will go in a zig zag pattern
        #'up_down' controls the direction (down and up) of movement across the rails
        up_down = None
        row, col = 0,0

        #Loop over each character position in the ciphertext
        for i in range(len(cipher)):
            #If I'm at the top rail, start moving down
            if row == 0:
                up_down = True
            #If I'm at the bottom rail, start moving up
            elif row == rails -1:
                up_down = False

            #Mark this position with '*' to indicate a letter goes here
            rail[row][col] = '*'
            #Move to the next column
            col += 1
            #Move up or down depending on current direction
            row = row +1 if up_down else row -1

        #Step 3: Fill the '*' positions with actual letters from the cipher text
        index = 0
        for i in range(rails): #Go through each rail
            for j in range(len(cipher)):#Go through each column
                #If I see a '*', replace it with the next ciphertext letter
                if(rail[i][j] == '*') and (index < len(cipher)):
                    rail[i][j] = cipher[index]
                    index += 1#Move to next letter in ciphertext

        #Step 4: Read the matrix in zigzag order to reconstruct the plaintext
        result = []#This will store the final decrypted message
        row, col = 0,0

        for i in range(len(cipher)):
            #Change direction when reaching the top or bottom rail
            if row == 0:
                up_down = True
            elif row == rails - 1:
                up_down = False

            #If the current cell is not empty, add the character to result
            if(rail[row][col] != '\n'):
                result.append(rail[row][col])
                col += 1 #Move to next column

            #Move up or down depending on current direction
            row = row + 1 if up_down else row -1

        #Step 5: Join the list of decrypted letters into one continuous plaintext message
        decrypted = "".join(result)

        #Return the decrypted text so it can be used elsewhere in the program
        print("--------------------------------------------------------------------")
        print(f"\nDecrypted Message: {decrypted}")
        print("\n--------------------------------------------------------------------")

        return decrypted
    #=========================================================================
    #End of Rail Fence Cipher - Decryption Function
    #=========================================================================

    def RFCMenu(self):
        while True:
            rails = 3 #Default rail count but will be overridden by user input

            #Display the main menu options to the user
            print("""\nWhat would you like to do?
    1. Encrypt a message
    2. Decrypt a message
    3. Exit
    """)

            #Damien: Added try/except to handle invalid (non-numeric) inputs
            try:
                userInput = int(input("Enter a choice: "))
            except ValueError:
                print("Invalid Input! Please select valid choice.\n")
                continue#Loops back to the menu instead of crashing

            #match-case used for menu options
            match userInput:
                case 1:
                    try:
                        # Damien: Added clear input prompt with better instruction
                        user_key = int(input("-----------------\nEnter key (number of rails): "))
                        #Get message to encrypt and remove any accidental extra spaces
                        user_message = input("Enter message to be encrypted: ").strip()

                        #Damien: Prevent encryption of empty messages
                        if len(user_message) < 1:
                            print("\nMessage cannot be empty.")
                            continue

                        rails = user_key
                        #Perform encryption
                        self.railfence_encryption(rails, user_message)
                    except ValueError:
                        #Damien: Prevent crash if non-integer key is entered
                        print("\nInvalid Input! Key must be a number. ")

                    # if user_key >= rails and len(user_message) >= len(message):
                    #     rails = user_key
                    #
                    #     railfence_encryption(rails, user_message)
                    #     break
                    # else:
                    #     print(
                    #         "\nNot a valid input. Key size must be greater than 3 and message must be more than 21 letters."
                    #     )
                case 2:
                    try:
                        user_key = int(input("-----------------\nEnter key (number of rails): "))

                        #Damien: Added validation to ensure a minimum of 2 rails
                        if user_key < 2:
                            print("\nKey must be at least 2. ")
                            continue
                        #Get message tp decrypt
                        user_message = input("Enter message to be decrypted: ").strip()
                        #Damien: Prevent decryption of empty messages
                        if len(user_message) < 1:
                            print("\nMessage cannot be empty.")
                            continue

                        rails = user_key
                        #Perform decryption
                        self.railfence_decryption(rails, user_message)
                    except ValueError:
                        #Damien: Prevent crash if non-integer key is entered
                        print("\nInvalid Input! Key must be a number. ")
                        # if user_key >= rails and len(user_message) >= len(message):
                        #     rails = user_key
                        #
                        #     railfence_decryption(rails, user_message)
                        #     break
                        # else:
                        #     print(
                        #         "\nNot a valid input. Key size must be greater than 3 and message must be more than 21 letters."
                        #     )
                case 3:
                    #Damien: Added user feedback message before exiting
                    print("Goodbye! ^_^")
                    exit()
                case _:
                    #Damien: Added fall back for invalid menu options
                    print("\nInvalid Choice! Please select available choices.")

#Damien: Created a new RailFenceCipher object, then calls its menu through that object (this will be used in main.py)
if __name__ == "__main__":
    RailFenceCipher().RFCMenu()