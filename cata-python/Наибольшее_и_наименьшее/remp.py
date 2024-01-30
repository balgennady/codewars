numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"
lst = []

# for function in (max, min):
for function in (max,):
    val = function(numbers.split(), key=int)
    lst.append(val)

max_str = str(lst[0])
# min_str = str(lst[1])

# print(max_str + ' ' + min_str)
print(max_str)
