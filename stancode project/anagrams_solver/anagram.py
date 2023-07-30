"""
File: anagram.py
Name:Ray
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
dictionary = set()


def main():
    """
    find all the anagrams that user input and print the anagram if it in the dictionary
    """
    read_dictionary()
    while True:
        print("Welcome to stanCode ''Anagram Generator'' (or -1 to quit)")
        s = str(input("Find anagrams for: "))
        start = time.time()
        if s == "-1":
            break
        find_anagrams(s)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as file:
        for line in file:
            dictionary.add(line.strip())


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    anagrams = []
    char_count, counter = get_char_count(s)
    backtrack("", char_count, anagrams, counter)
    print(len(anagrams), "anagrams:", anagrams)


def get_char_count(s):
    char_count = {}
    counter = 0
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        counter += 1
    return char_count, counter


def backtrack(current_word, char_count, anagrams, counter):
    if len(current_word) == counter:
        if current_word in dictionary:
            anagrams.append(current_word)
            print("Searching...")
            print("Found:", current_word)
    else:
        for char in char_count:
            if char_count[char] > 0:
                # choose
                char_count[char] -= 1
                # explore
                backtrack(current_word + char, char_count, anagrams, counter)
                # un-choose
                char_count[char] += 1


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
