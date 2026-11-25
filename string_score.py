"""
File: string_score.py
Name:
------------------------------
This program calculates a score for a given string based on
the types of characters it contains.

Digits are worth 1 point, uppercase letters are worth 2 points,
and lowercase letters are worth 3 points. The score() function
iterates through each character in the string, adds up the
corresponding points, and prints the final total score.
"""


def main():
    """
    TODO:
    """
    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    score = 0

    for i in range(len(string)):
        ch = string[i]

        if ch.isdigit():
            score = score + 1

        elif ch.isupper():
            score = score + 2

        elif ch.islower():
            score = score + 3

    print(score)



if __name__ == '__main__':
    main()