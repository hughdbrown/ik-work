#!/usr/bin/env python3

def find_first_occurrence(source, target):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    >>> find_first_occurrence("interview", "e")
    3
    >>> find_first_occurrence("kickstart", "n")
    -1
    """
    return source.find(target)


if __name__ == '__main__':
    from doctest import testmod
    print("Run 2 passing tests")
    testmod()
    print("Tests done")
