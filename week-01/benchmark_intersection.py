#!/usr/bin/env python3

from collections import Counter
from datetime import datetime
from random import randint

def intersection_1(a, b):
    ac = Counter(a)
    bc = Counter(b)
    result = []
    for k, v in ac.items():
        count = min(v, bc.get(k, 0))
        result.extend([k] * count)
    return result

def intersection_4(a, b):
    ac = Counter(a)
    bc = Counter(b)
    result = []
    for k, v in ac.items():
        if k in bc:
            count = min(v, bc[k])
            result.extend([k] * count)
    return result

def intersection_2(a, b):
    ac = Counter(a)
    bc = Counter(b)
    result = []
    keys = set(ac).intersection(bc)
    for k in keys:
        count = min(ac[k], bc[k])
        result.extend([k] * count)
    return result

def intersection_3(a, b):
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
            if ac[i] < bc[j]:
                while i < len(ac) and ac[i] < right:
                    i += 1
            else:
                while j < len(bc) and bc[j] < left:
                    j += 1

    return result

def main():
    funcs = [intersection_1, intersection_2, intersection_3, intersection_4]
    data_a = [randint(0, 1000) for _ in range(10000000)]
    data_b = [randint(0, 1000) for _ in range(10000000)]

    for size in [100, 1000, 10000, 100000, 1000000, 10000000]:
        a = data_a[:size]
        b = data_b[:size]
        print(f"{'-' * 30} {size = }")

        for fn in funcs:
            start = datetime.now()
            r = fn(a, b)
            end = datetime.now()
            print(f"{fn.__name__} {end - start} {sum(r)}")


if __name__ == '__main__':
    main()
