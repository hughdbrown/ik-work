#!/usr/bin/env python3

def uppercase_to_lowercase(s):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    >>> uppercase_to_lowercase('')
    ''
    >>> uppercase_to_lowercase('HELLO')
    'hello'
    >>> uppercase_to_lowercase('hello')
    'hello'
    """
    return s.lower()


if __name__ == '__main__':
    from doctest import testmod
    print("Run 3 passing tests")
    testmod()
    print("Tests done")
