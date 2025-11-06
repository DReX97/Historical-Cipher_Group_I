"""
origninal link :https://github.com/palash25/pyphers/blob/master/atbashCipher.py
accessed on the 4/11/2025
edited by Ross Prizeman

changes made :
- improved from a dictionary lookup to a easier and safer transform
- not dependent on input being all uppercase characters
- can use both upper and lower case characters
- still uses the hardcoded example
- added a menu
- no longer uses hard coded example
- takes user input
- no longer have to run the file again to encrypt/ decrypt more than one input
- also gives an error message if the user enters an invalid option when asked if they would like to encrypt decrypt or exit
- now it is in a class
- no longer just a file with functions
- able to be called in the main.py file
"""

class AtbashCipher:
    def __init__(self):
        self.name = "Atbash Cipher"

    def atbash(self, text):
        result = ""
        for ch in text:
            if 'A' <= ch <= 'Z':
                result += chr(ord('Z') - (ord(ch) - ord('A')))
            elif 'a' <= ch <= 'z':
                result += chr(ord('z') - (ord(ch) - ord('a')))
            else:
                result += ch
        return result
#Hard-coded driver function to run the program


    def AtMenu(self):
        while True:
            print(f"""\n===  {self.name} ===
    1. Encrypt a message
    2. Decrypt a message
    3. Exit
    """)
            # Get a valid numeric choice
            try:
                choice = int(input("Enter a choice: ").strip())
            except ValueError:
                print("Invalid input! Please enter 1, 2, or 3.\n")
                continue

            if choice == 1:
                # Encrypt (same operation as decrypt)
                text = input("Enter message to encrypt: ")
                print("\nResult:", self.atbash(text))
            elif choice == 2:
                # Decrypt (same operation as encrypt)
                text = input("Enter message to decrypt: ")
                print("\nResult:", self.atbash(text))
            elif choice == 3:
                print("thank you")
                break
            else:
                print("Invalid choice! Please select 1, 2, or 3.\n")


# Executes the main function
if __name__ == "__main__":
    AtbashCipher().Atmenu()
