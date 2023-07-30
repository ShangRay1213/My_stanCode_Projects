"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 1


def main():
    """
    pre-condition:build each parts of rocket
    post-condition:Combine all the parts of rocket
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    make rocket's head
    """
    a = SIZE
    for i in range(SIZE, 0, -1):
        print(' ' * i, end='')
        print('/' * ((a+1)-i), end='')
        print("\\" * ((a+1)-i))


def belt():
    """
    make rocket's belt
    """
    ans = ''
    for i in range(SIZE*2):
        ans += "="
    print("+" + str(ans) + "+")


def upper():
    """
    The upper body of the rocket
    """
    a = SIZE
    for i in range(SIZE, 0, -1):
        print("|", end='')
        print("."*(i-1), end='')
        print("/\\"*((a+1)-i), end='')
        print("." * (i - 1), end='')
        print("|")


def lower():
    """
    The lower body of the rocket
    """
    a = SIZE
    for i in range(SIZE, 0, -1):
        print("|", end='')
        print("." * (a - i), end='')
        print("\\/"*i, end='')
        print("." * (a - i), end='')
        print("|")


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
