def zeros(n):
    a = 1
    res = 0
    while 5**a < n:
        res += n // 5**a
        a += 1
    return res

def zeros4(n):
    zeros = 0
    i = 5
    while n//i > 0:
        zeros += n//i
        i*=5
    return zeros

def zeros2(n):
  x = n/5
  return x + zeros2(x) if x else 0

def zeros3(n):
    """
        Ни у одного факториала не будет меньше нулей, 
        чем у факториала с меньшим числом.

        Каждое кратное 5 добавляет 0, поэтому сначала мы посчитаем, 
        сколько кратных 5 меньше `n` (`n // 5`).

        Каждое кратное 25 добавляет два 0, поэтому затем мы добавляем еще 0 
        для каждого кратного 25 меньше n.

        Продолжаем для всех степеней 5, меньших (или равных) n.
    """
    pow_of_5 = 5
    zeros = 0
    
    while n >= pow_of_5:
        zeros += n // pow_of_5
        pow_of_5 *= 5
        
    return zeros

print(zeros(100))
