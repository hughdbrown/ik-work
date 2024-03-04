#!/usr/bin/env python3

from collections import Counter

def get_intersection_with_maintained_frequency(a, b):
    """
    Args:
     a(list_int32)
     b(list_int32)
    Returns:
     list_int32
    >>> get_intersection_with_maintained_frequency([], [])
    []
    >>> get_intersection_with_maintained_frequency([], [1, ])
    []
    >>> get_intersection_with_maintained_frequency([1, ], [])
    []
    >>> get_intersection_with_maintained_frequency([], [1, 1, 1, 1, ])
    []
    >>> get_intersection_with_maintained_frequency([4, 2, 2, 3, 1], [2, 2, 2, 3, 3])
    [2, 2, 3]
    >>> get_intersection_with_maintained_frequency([6, 2, 4], [1, 5, 3, 7])
    []
    """
    # Write your code here.
    ac = Counter(a)
    bc = Counter(b)
    result = []
    for k, v in ac.items():
        result.extend([k] * min(v, bc.get(k, 0)))
    return result 


if __name__ == '__main__':
    from doctest import testmod
    print("Run 5 passing tests")
    testmod()
    print("Tests done")
