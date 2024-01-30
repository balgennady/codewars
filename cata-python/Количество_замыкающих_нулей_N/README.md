# Number of trailing zeros of N!

[text](https://www.codewars.com/kata/52f787eb172a8b4ae1000a34)

## Details

Напишите программу, которая будет рассчитывать количество конечных нулей в факториале заданного числа.

    N! = 1 * 2 * 3 * ... * N

Быть осторожен 1000! имеет 2568 цифр...

For more info, see: http://mathworld.wolfram.com/Factorial.html

## Example

```py
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
```

## Note

Вы не должны рассчитывать факториал. Найдите другой способ узнать количество нулей.
