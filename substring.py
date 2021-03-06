#!/usr/bin/env python
from sys import argv

def substring(word):
    """

---

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .

Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.

The game ends when both players have made all possible substrings.
 
Scoring
A player gets +1 point for each occurrence of the substring in the string.
 
For Example:

String = BANANA

Kevin's vowel beginning word = ANA


Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

---

Alice and Bob want to play the following game:

* Game Rules

Both players are given the same string composed only of capital letters.

Both players have to make substrings using the letters of the string. 

    Alice has to make words starting with consonants.
    Bob has to make words starting with vowels.

The game ends when both players have made all possible substrings.

* Scoring

A player gets +1 point for each unique substring.

* Example

SCIENCE

Alice (17)
    S, C, N, SC, CI, NC, CE, SCI, CIE, NCE, SCIE, CIEN, SCIEN, CIENC, SCIENC, CIENCE, SCIENCE
    
Bob (9)
    I, E, EI, EN, IEN, ENC, IENC, ENCE, IENCE
    
* Write a function game_outcome(word) that returns a string with the winner and their score, e.g. 'Alice 17', or 'Draw' if there is a draw. 

"""
    print(word)


if __name__ == "__main__":
    if len(argv) == 2:
        substring(argv[1])
        exit(0)
    else:
        print("Usage: %s <word>" % argv[0])
        exit(1)
