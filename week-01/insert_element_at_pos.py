#!/usr/bin/env python3

def insert_element_at_position(nums, element, position):
    """
    Args:
     nums(list_int32)
     element(int32)
     position(int32)
    Returns:
     list_int32
    >>> insert_element_at_position([-1], 12, 0)
    [12]
    >>> insert_element_at_position([2, 4, 5, 6, -1], 3, 2)
    [2, 3, 4, 5, 6]
    >>> insert_element_at_position([70, 60, 50, -1], 40, 4)
    [70, 60, 50, 40]
    """
    # Write your code here.
    last_elem = position == len(nums)
    position -= 1
    if last_elem:
        nums[position] = element
    else:
        nums = nums[ : position] + [element] + nums[position : -1] 
    return nums


if __name__ == '__main__':
    from doctest import testmod
    print("Run 3 passing tests")
    testmod()
    print("Tests done")
