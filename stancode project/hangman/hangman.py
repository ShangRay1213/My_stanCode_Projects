"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
     pre-condition: make a random word to let you guess
     post-condition: tell you if you guess that word or not
    """
    ans = random_word()
    user_ans = dashed(ans)
    print("The word looks like " + str(user_ans))
    life = N_TURNS
    while life != 0 and user_ans != ans:
        n = str(input("Your guess: "))
        if n.islower():
            n = n.upper()
        if not n.isalpha() or len(n) != 1:
            print("illegal format.")
        else:
            user_ans = compare(user_ans, ans, n)
            if n not in ans:
                life = life-1
            if life != 0 and user_ans != ans:
                print("The word looks like " + str(user_ans))
                print("You have " + str(life) + " wrong guesses left")
    if user_ans == ans:
        print("You win!!")
        print("The word was: " + str(ans))
    else:
        print("You are completely hung :(")
        print("The word was " + str(ans))


def compare(user_ans, ans, n):
    """
    to know that if the User answer are same with the coder answer
    """
    new_dashed = ''
    if n in ans:
        print("You are correct!!")
        for i in range(len(ans)):
            if n == ans[i]:
                new_dashed += ans[i]
            else:
                new_dashed += user_ans[i]
    else:
        print("There is no " + str(n) + "'s" + " in the word.")
        return user_ans
    return new_dashed


def random_word():
    """
    choose the word
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def dashed(ans):
    """
    pre-condition:shows how many letters
    post-condition:show the letter that you already guess it
    """
    new = ''
    for i in range(len(ans)):
        new += "-"
    return new

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
