def find_it(seq):

    d = {}

    for i in seq:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    for key, value in d.items():
        if value % 2 != 0:
            return key
    
    return False
