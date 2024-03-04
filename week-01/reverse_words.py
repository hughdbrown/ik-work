#!/usr/bin/env python3

def reverse_words(s):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    >>> reverse_words("")
    ''
    >>> reverse_words("blue")
    'blue'
    >>> reverse_words("blue sky")
    'sky blue'
    >>> reverse_words("sky blue")
    'blue sky'
    >>> reverse_words("best technical interview prep courses")
    'courses prep interview technical best'
    """
    # Write your code here.
    words = list(s.split(" "))
    words.reverse()
    return " ".join(words)


if __name__ == '__main__':
    from doctest import testmod
    print("Run 5 passing tests")
    testmod()
    print("Tests done")
