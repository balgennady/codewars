l = [5, 1, 4, 5, 4, 5, 1]

d = {}

for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
for key, value in d.items():
    if value % 2 != 0:
        print(key)
