"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Encrypt with Caesar cipher
    """
    new_alphabet()


def new_alphabet():
    """
    to Encrypt the words
    """
    n = int(input("Secret number: "))
    w = str(input("What's the ciphered string?"))
    a = ' '
    if w.islower():
        w = w.upper()
    ans = ''
    for i in range(len(w)):
        index = w[i]
        s = ALPHABET.find(index)
        if s != (-1):
            if (s+n) < 26:
                ans += ALPHABET[s+n]
        if s != (-1):
            if (s+n) >= 26:
                y = (s+n)-26
                ans += ALPHABET[y]
        if index == a:
            ans += a
        if s == -1:
            ans += index
    print("The deciphered string is: " + str(ans))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
