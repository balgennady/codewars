def findNextSquare(sq):
    '''Возвращает следующий идеальный квадрат'''

    return ((sq**0.5)+1)**2 if (sq**0.5)%1 == 0 else -1


def findNextSquare_(sq):
    '''Возвращает следующий идеальный квадрат'''
    x = sq**0.5
    return int((x+1)**2) if x % 1 == 0 else -1

print(findNextSquare_(625))
