#!/usr/bin/env python3
from string import ascii_letters
from collections import Counter

def count_alphabets(s):
    """
    Args:
     s(str)
    Returns:
     int32
    >>> count_alphabets("")
    0
    >>> count_alphabets("a")
    1
    >>> count_alphabets("A")
    1
    >>> count_alphabets("Aa")
    2
    >>> count_alphabets("aAAa")
    4
    >>> count_alphabets("#aBdj12C")
    5
    >>> count_alphabets("123 !@#$")
    0
    >>> count_alphabets("aa AA 11   @# ")
    4
    """
    c = Counter(s)
    valid_alpha = set(ascii_letters)
    return sum(v for k, v in c.items() if k in valid_alpha)


if __name__ == '__main__':
    from doctest import testmod
    print("Run 7 passing tests")
    testmod()
    print("Tests done")
