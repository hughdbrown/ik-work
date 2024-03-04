#!/usr/bin/env python3

def length_of_last_word(sentence):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    >>> length_of_last_word('')
    0
    >>> length_of_last_word('interview')
    9
    >>> length_of_last_word('interview kickstart')
    9
    >>> length_of_last_word('interview kick start')
    5
    >>> length_of_last_word('interview start kick')
    4
    >>> length_of_last_word(" Hello World  ")
    5
    """
    words = (s.strip() for s in sentence.split(" "))
    real_words = [word for word in words if word]
    return 0 if not real_words else len(real_words[-1])


if __name__ == '__main__':
    from doctest import testmod
    print("Run 6 passing tests")
    testmod()
    print("Tests done")
