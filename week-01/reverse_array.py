#!/usr/bin/env python3

def reverse_array(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    >>> reverse_array([])
    []
    >>> reverse_array([1])
    [1]
    >>> reverse_array([1, 2])
    [2, 1]
    >>> reverse_array([2, 1])
    [1, 2]
    >>> reverse_array([4] * 4)
    [4, 4, 4, 4]
    """
    # Write your code here.
    return list(nums)[::-1]


if __name__ == '__main__':
    from doctest import testmod
    print("Run 5 passing tests")
    testmod()
    print("Tests done")
