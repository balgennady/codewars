# вводим N
# n = input("n=")

# Листинг 1
def prim1(n):

    lst = []    # пустой список для хранения простых чисел
    k = 0       # в k будем хранить количество делителей
    
    # пробегаем все числа от 2 до N
    for i in range(2, n+1):
        
        # пробегаем все числа от 2 до текущего
        for j in range(2, i):
            # ищем количество делителей
            if i % j == 0:
                k = k + 1
        # если делителей нет, добавляем число в список
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst

# Листинг 2
def prim2(n):

    lst = []    # пустой список для хранения простых чисел

    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break   # если делитель найден, число не простое.
        else:
            lst.append(i)
    return lst

# Листинг 3
def prim3(n):

    lst = []

    for i in range(2, n+1):
        # пробегаем по списку (lst) простых чисел
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)

    return lst

from math import sqrt
# Листинг 4 
def prim4(n):

    lst=[]

    for i in range(2, n+1):
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    
    return lst

# Листинг 6 
def prim6(n):

    lst = [2] # заносим в выходной массив 2

    for i in range(3, n+1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    
    return lst
    
# Решето Эратосфена
def prim5(n):
    
    a = [x for x in range(n+1)]
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    return lst


def is_prime(n):
    for i in range(2, int(n**.5 + 1)):
        if n % i == 0:
            return False
    return True

    
print(prim6(50))
