def tickets(people):
    cassa = []
    for man in people:
        if len(cassa) == 0 and man > 25:
            return "в кассе нет сдачи"
        if man == 25:
            cassa.append(man)
            cassa.sort(reverse=True)
        elif man > 25:
            sdacha = man - 25
            for i in range(0, len(cassa)):
                if cassa[i] == sdacha:
                    cassa.remove(sdacha)
                    cassa.append(man)
                    cassa.sort(reverse=True)
                    break
                elif cassa[i] > sdacha:
                    continue
                elif cassa[i] < sdacha:
                    sdacha -= cassa[i]
                    cassa.remove(cassa[i])
                    continue
                    # return "net deneg"
    return cassa

print( tickets( [25, 50, 25, 100]) )
# print( tickets( [25, 50, 25, 50, 50, 25, 25, 100]) )
