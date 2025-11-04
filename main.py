"""
main.py

Historical Cipher Group I
Author: Damien Ho
Accessed: 04 Nov 2025

Description:
This is the main driver program for the group project.
It allows users to choose between different classical ciphers:
    -Rail Fence Cipher (Implemented by Damien Ho)
    -Caesar Cipher (Implemented by Connor Reid)
    -Atbash Cipher (Implemented by Ross Prizeman)

Damien's Contributions:
    -Created the main CLI menu system
    -Integrated Rail Fence Cipher (wrapped class structure)
    -Improved exit logic for Rail Fence to return users back to main menu.
"""
from rail_fence_cipher import RailFenceCipher #Damien: Importing my wrapped Rail Fence Cipher class

#==========================================================
#Main Menu function
#Damien: Displays the overall project menu and lets users choose which cipher they want to use
#==========================================================
def main():

    print("Welcome to Historical Cipher Group I!")
    print("This program will include Rail Fence, Caesar, and Vigenere ciphers.")

    while True:
        print("""\n
=======================
Historical Cipher Menu
=======================
1. Rail Fence Cipher
2. Caesar Cipher
3. Atbash Cipher
4. Exit
    """)
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            rail_menu()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            print("Goodbye! Thank you for using our application! ^_^")
            break
        else:
            print("\nInvalid choice! Please enter 1 - 4. ")

#==========================================================
#Rail Fence Cipher Integration
#Damien: Calls the RailFenceCipher class and runs its menu.
#On exit, control returns back to the main menu.
#==========================================================
def rail_menu():
    cipher = RailFenceCipher()#create instance
    cipher.RFCMenu()#call the wrapped class menu

#Entry Point
if __name__ == "__main__":
    main()