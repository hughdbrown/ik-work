#!/usr/bin/env python3

def get_pivot_index(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    >>> get_pivot_index([2, 3, 1, -1, 1, 1, 4])
    2
    >>> get_pivot_index([2, 3, 5])
    -1
    >>> get_pivot_index([0, -1, 1])
    0
    """
    # Write your code here.
    left = 0
    right = sum(nums)
    for i, x in enumerate(nums):
        right -= x
        if i > 0:
            left += nums[i - 1]
        if left == right:
            return i
    return -1


if __name__ == '__main__':
    from doctest import testmod
    print("Run 3 passing tests")
    testmod()
    print("Tests done")
