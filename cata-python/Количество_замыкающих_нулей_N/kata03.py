def find_it(seq):

    for i in seq:
        if seq.count(i)%2!=0:
            return i

def find_it2(seq):
    return [x for x in seq if seq.count(x) % 2][0]
