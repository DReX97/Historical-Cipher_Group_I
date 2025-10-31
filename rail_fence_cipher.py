"""
Original Source: https://github.com/ekcaroline/Classical-Ciphers-Railfence/blob/main/railfence_encrypt.py
Accessed: 30 Oct 2025
Modified by Damien Ho

Description:
This is the baseline Rail Fence Cipher implementation originally sourced from GitHub.
My Contribution includes:
-Implemented decryption function.
-Integrate with main.py for group project demo.
"""
import string


def railfence_encryption(rails, message):
    print("\nWe will now began to perform the railfence cipher. ")

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
    print(f"\nEncrypted message: {format_enc_message}")

    # Show grid
    userChoice = input("\nWould you like to see the grid? (Y/N) ")
    if userChoice.lower() == "y":
        for row in fence:
            print(''.join(row))
    else:
        print("Okay, thank you for using the railfence cipher.")

#=========================================================================
# Rail fence decryption function
#Author: Damien Ho
#Description:
#           This function performs decryption for the Rail Fence Cipher.
#           It reconstructs the zig zag pattern used during encryption,
#           fills the matrix with ciphertext letters in the correct order,
#           and then reads the message diagonally to reveal the plaintext.
#=========================================================================
def railfence_decryption(rails, cipher):#I renamed the variable in the parameter from user_message to cipher to make the code more semantically correct and easier to understand personally.
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
    print(f"\nDecrypted Message: {decrypted}")

    return decrypted
#=========================================================================
#End of Rail Fence Cipher - Decryption Function
#=========================================================================

def menu():
    while True:
        rails = 3
        message = "Programmingisfun!"

        userInput = int(input("""What would you like to do?
1. Encrypt a message
2. Decrypt a message
3. Exit

Enter a choice: """))

        match userInput:
            case 1:
                user_key = int(input("-----------------\nEnter key: "))
                user_message = input(
                    "Enter message to be encrypted (more than 21 letters): ")

                if user_key >= rails and len(user_message) >= len(message):
                    rails = user_key

                    railfence_encryption(rails, user_message)
                    break
                else:
                    print(
                        "\nNot a valid input. Key size must be greater than 3 and message must be more than 21 letters."
                    )
            case 2:
                user_key = int(input("-----------------\nEnter key: "))
                user_message = input(
                    "Enter message to be decrypted (more than 21 letters): ")

                if user_key >= rails and len(user_message) >= len(message):
                    rails = user_key

                    railfence_decryption(rails, user_message)
                    break
                else:
                    print(
                        "\nNot a valid input. Key size must be greater than 3 and message must be more than 21 letters."
                    )
            case 3:
                exit()


print(
    "Welcome! This Python program takes a user-provided key and message, then encrypts the message using the Rail Fence Cipher. It creates a matrix to represent the zigzag pattern and fills it with the message's characters. The resulting matrix is printed, showing the encrypted message in a Rail Fence pattern. The program ensures user inputs meet the criteria for a valid encryption.\n"
)
menu()