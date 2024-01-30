

# paying - платеж

def tickets(people):

    bank = []
    cost = 25
    
    for paying in people:

        if paying > cost and len(bank) == 0:
            return "NO"
        elif paying == cost:
            bank.append(paying)
            bank.sort()
        
        else:
            # определяем сумму сдачи
            delivery = paying - cost 
            # выдаем сдачу из имеющихся денег
            
            # если сдача равна последней купюре
            if delivery == bank[-1]:
                bank.remove(bank[-1])
                bank.append(paying)
            # если сдача больше последней купюры
            elif delivery > bank[-1]:
                for i in bank[::-1]:
                    delivery -= i
                    bank.remove(i)
                # если сдача меньше чем последняя купюра
                elif delivery < bank[-1]:
                    for i in bank[::-1]:
                        if i > delivery:
                            continue          
                        elif delivery == i:
                            bank.remove(i)
                            bank.append(paying)
                            break
                        else:
                            delivery = delivery - i
                            bank.remove(i)
            # если сдача меньше последней купюры
            else:
                return "NO"
    return "YES"

# print(tickets([50, 50, 50, 50, 50, 50, 50, 50, 50, 50]))
print(tickets([25, 50, 25, 50, 100]))
# print(tickets([25, 25, 25, 50, 50, 25, 100]))
