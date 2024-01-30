def high_and_low(list_str):
    list_num = [int(x) for x in list_str.split()]
    list_num.sort()
    return "{} {}".format(list_num[-1], list_num[0])

def high_and_low2(numbers):
    n = map(int, numbers.split(' '))
    return "{} {}".format(max(n), min(n))

def high_and_low3(numbers):
    return " ".join( x(numbers.split(), key=int) for x in (max, min) )
    '''
        если изменить «x» на «function», это может быть более читабельно:
            function(numbers.split(), key=int) for function in (max, min)
        или что то же самое:
            for function in (max, min):
                function(numbers.split(), key=int)
        Поскольку функции в Python являются объектами, их можно повторять, 
        поэтому он выполняет итерацию набора, содержащего две функции, min и max, 
        и применяет к ним один и тот же аргумент, 
        поэтому в результате получается список, содержащий только 2 элемента: min и max.
    '''

print(high_and_low3("1 9 3 4 -5"))
