def tickets(people):
    if len(people) == 0:
        return "NO"
    if people[0] == 0:
        return "NO"
    cassa = []
    for man in people:
        if len(cassa) == 0 and man > 25:
            return "NO"
        if man == 25:
            cassa.append(man)
            cassa.sort(reverse=True)
        elif man > 25:
            balance = man - 25
            i = 0
            while(len(cassa) != 0):
                if cassa[i] == balance:
                    cassa.remove(cassa[i])
                    cassa.append(man)
                    cassa.sort(reverse=True)
                    break
                elif cassa[i] > balance:
                    i += 1
                elif cassa[i] < balance:
                    balance -= cassa[i]
                    cassa.remove(cassa[i])
                    continue
                else: return "NO"
    return "YES"

# print( tickets( [25, 25, 50] ) )
print( tickets( [25, 100] ) )
# print( tickets( [25, 50, 25, 50, 50, 25, 25, 100]) )
