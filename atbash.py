"""
origninal link :https://github.com/palash25/pyphers/blob/master/atbashCipher.py
accessed on the 4/11/2025
edited by Ross Prizeman

changes made :
- improved from a dictionary lookup to a easier and safer transform
- not dependent on input being all uppercase characters
- can use both upper and lower case characters
- still uses the hardcoded example
"""
def atbash(text):
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr(ord('Z') - (ord(ch) - ord('A')))
        elif 'a' <= ch <= 'z':
            result += chr(ord('z') - (ord(ch) - ord('a')))
        else:
            result += ch
    return result
# Hard-coded driver function to run the program


def main():
    message = 'ALICE KILLED BOB'
    print(atbash(message.upper()))

    message = 'ZORXV PROOVW YLY'
    print(atbash(message.upper()))


# Executes the main function
if __name__ == '__main__':
    main()