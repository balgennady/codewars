# Кому это нравится?

хранить количество имен в `n = len(names)`

подготовить словарь для всех случаев:

```py
{
    0: 'no one likes this',
    1: '{} likes this',
    2: '{} and {} like this',
    3: '{}, {} and {} like this',
    4: '{}, {} and {others} others like this'
}
```

получить значение для словаря с ключём `n`, если `n > 4` получить значение для ключа `4` ( `min(4, n)`

next working with string for example `{}, {} and {others} others like this` and format function

`format(*names[:3])` is same as `format(names[0], names[1], names[2])`. If names count less then 3 for example has one element `format(*names[:3])` equal to `format(names[0])`, and we apply named placeholder others passing `others=n-2` into format

so `names['a', 'b']`

```py
n = 2
string = '{} and {} like this' (dict[min(4,2)])
```

and `format(names[:3], others=n-2)` equal to `format('a', 'b', others=0)`

finally it eq: `{} and {} like this`.`format('a', 'b', others=0)`; no others placeholder in string so we skipping it. So it will be `a and b like this`
