# Find The Parity Outlier

[text](https://www.codewars.com/kata/5526fc09a1bbd946250002dc)

## Details

Вам дан массив (который будет иметь длину не менее 3, но может быть очень большим), содержащий целые числа. Массив либо целиком состоит из нечетных целых чисел, либо целиком состоит из четных целых чисел, за исключением одного целого числа `N`. 

Напишите метод, который принимает массив в качестве аргумента и возвращает этот «выброс» `N`.

## Examples

```py
[2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)
```
