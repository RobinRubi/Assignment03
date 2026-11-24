"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to solve a real-world
problem: finding the complementary strand of a DNA sequence.

The program provides different DNA sequences as Python strings.
These strings are case-sensitive, and your task is to generate
and output the correct complementary strand for each sequence.
"""


def main():
    """
    TODO:
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    ans = ""
    if dna == "":
        return "DNA strand is missing."

    for i in range(len(dna)):
        ch = dna[i]

        if ch == "A":
            ans = ans + "T"

        elif ch == "T":
            ans = ans + "A"

        elif ch == "C":
            ans = ans+ "G"

        else:
            ans = ans + "C"

    return ans




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
