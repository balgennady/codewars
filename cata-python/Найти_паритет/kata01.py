lst = [2, 4, 0, 100, 4, 11, 2602, 36]

print(lst)

even =  [ x for x in lst if (x % 2 == 0) ]
odd =   [ x for x in lst if (x % 2 != 0) ]

if len(even) > len(odd):
    print (odd)
else:
    print (even)

def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
