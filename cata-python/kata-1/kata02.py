def tickets(people):

    if sum(people) == 0: return "NO"
    if len(people) == 0: return "NO"

    maney_25  = 0
    maney_50  = 0
    maney_100 = 0

    for i in people:

            if i == 25:
                maney_25 += 1
            elif i == 50:
                if maney_25 >= 1:
                    maney_25 -= 1
                    maney_50 += 1
                else:
                    return "NO"
            elif i == 100:
                # здача 50 25
                if maney_50 >= 1 and maney_25 >= 1:
                    maney_25 -= 1
                    maney_50 -= 1
                    maney_100 += 1
                # здача 25 25 25
                elif maney_25 >= 3:
                    maney_25 -= 3
                    maney_100 += 1
                else:
                    return "NO"
    return "YES"

print( tickets( [25, 50, 25, 50, 100] ) )
# print( tickets( [25, 25, 50] ) )
