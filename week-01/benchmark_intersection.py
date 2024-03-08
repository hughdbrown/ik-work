#!/usr/bin/env python3

from collections import Counter
from datetime import datetime
from random import randint

def intersection_1(a, b):
    # Counted hashtable approach
    # O(n)
    ac = Counter(a)
    bc = Counter(b)
    result = []
    for k, v in ac.items():
        count = min(v, bc.get(k, 0))
        result.extend([k] * count)
    return result

def intersection_2(a, b):
    # Counted hashtable approach
    # O(n)
    ac = Counter(a)
    bc = Counter(b)
    result = []
    for k, v in ac.items():
        if k in bc:
            count = min(v, bc[k])
            result.extend([k] * count)
    return result

def intersection_3(a, b):
    # Counted hashtable approach
    # O(n)
    ac = Counter(a)
    bc = Counter(b)
    result = []
    keys = set(ac).intersection(bc)
    for k in keys:
        count = min(ac[k], bc[k])
        result.extend([k] * count)
    return result

def intersection_4(a, b):
    # Two pointer method on sorted lists
    # Multiple loop increments
    # O(n logn)
    ac = sorted(a)
    bc = sorted(b)
    result = []
    i, j = 0, 0
    while i < len(ac) and j < len(bc):
        left, right = ac[i], bc[j]
        if left == right:
            result.append(left)
            i += 1
            j += 1
        else:
            if left < right:
                while i < len(ac) and ac[i] < right:
                    i += 1
            else:
                while j < len(bc) and bc[j] < left:
                    j += 1

    return result

def intersection_5(a, b):
    # Two pointer method on sorted lists
    # Single loop increment
    # O(n logn)
    ac = sorted(a)
    bc = sorted(b)
    result = []
    i, j = 0, 0
    while i < len(ac) and j < len(bc):
        left, right = ac[i], bc[j]
        if left == right:
            result.append(left)
            i += 1
            j += 1
        else:
            if left < right:
                i += 1
            else:
                j += 1

    return result


def intersection_6(a, b):
    # Naive iteration over lists
    # Modifies lists
    # time: O(n**3)
    result = []
    for a_item in a:
        for i, b_item in enumerate(b):
            if a_item == b_item:
                result.append(a_item)
                b.pop(i)
                break
    return result


def main():
    sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
    funcs = [intersection_1, intersection_2, intersection_3, intersection_4, intersection_5, intersection_6]
    data_a = [randint(0, 1000) for _ in range(sizes[-1])]
    data_b = [randint(0, 1000) for _ in range(sizes[-1])]

    for size in sizes:
        a = data_a[:size]
        b = data_b[:size]
        print(f"{'-' * 30} {size = }")

        for fn in funcs:
            start = datetime.now()
            r = fn(a, b)
            end = datetime.now()
            print(f"{fn.__name__} {end - start} {sum(r)} {len(r)}")


if __name__ == '__main__':
    main()
