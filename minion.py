#!/usr/bin/env python
from sys import argv

# Kevin and Stuart want to play the 'The Minion Game'.
# 
# Game Rules
# 
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
#
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
#
# The game ends when both players have made all possible substrings.
#  
# Scoring
# A player gets +1 point for each occurrence of the substring in the string.
#  
# For Example:
#
# String  = BANANA
# Kevin's vowel beginning word = ANA
#
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.


def minion(word):
    """
    """


if __name__ == "__main__":
    if len(argv) == 2:
        exit(0)
    else:
        print("Usage: %s <word>" % argv[0])
        exit(1)
