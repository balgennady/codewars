def find_outlier(integers):
    assert len(integers) >= 3

    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n

    assert False

l2 = [2, 4, 0, 100, 4, 11, 2602, 36]
find_outlier(l2)
