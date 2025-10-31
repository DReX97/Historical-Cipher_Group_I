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

    rail =[['\n' for i in range(len(cipher))] for j in range(rails)]

    up_down = None
    row, col = 0,0

    for i in range(len(cipher)):
        if row == 0:
            up_down = True
        elif row == rails -1:
            up_down = False

        rail[row][col] = '*'
        col += 1
        row = row +1 if up_down else row -1

    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if(rail[i][j] == '*') and (index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0,0

    for i in range(len(cipher)):
        if row == 0:
            up_down = True
        elif row == rails - 1:
            up_down = False

        if(rail[row][col] != '\n'):
            result.append(rail[row][col])
            col += 1

        row = row + 1 if up_down else row -1

    decrypted = "".join(result)

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