def gap(g,m,n):
    """Поиск интервала между простыми числами.
        
        Аргументы:
        - `g` -- длина пробела
        - `m` -- начало поиска (integer >= 2)
        - `n` -- конец поиска (integer >= `m`)
    """
    res_lst = []
    range_lst = []
    n_lst = prime(n)
    range_lst = [x for x in n_lst if x >= m]
    
    for x in range( 1, len(range_lst) ):
        if (range_lst[x] - range_lst[x-1]) == g:
            res_lst.append( range_lst[x-1] )
            res_lst.append( range_lst[x] )

    if len(res_lst) == 0:
        return None
    else: 
        return res_lst[0:2]
    
def prime(n):
    '''Возвращает все простые от 2 до `n`'''

    lst_prime = [2]

    for seed in range(3, n+1, 2):
        if (seed > 10) and (seed % 10 == 5):
            continue
        for i in lst_prime:
            if i*i-1 > seed:
                lst_prime.append(seed)
                break
            if (seed % i == 0):
                break
        else:
            lst_prime.append(seed) 
  
    return lst_prime

print( gap(2,100,110) )
