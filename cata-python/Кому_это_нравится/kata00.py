# составьте словарь d из всех возможных ответов.
# Ключи - это количество людей, которым это понравилось.
# {} указать заполнители. 
# Им не нужны никакие цифры, они просто заменяются/форматируются в том порядке, 
# в котором аргументы в именах приводятся в формате 
# {others} можно заменить его именем; ниже аргумента "others = length - 2"
# передается в str.format()
d = {
    0: "no one likes this",
    1: "{} likes this",
    2: "{} and {} like this",
    3: "{}, {} and {} like this",
    4: "{}, {} and {others} others like this"
    }
length = len(names)
# d[min(4, length)] гарантирует, что соответствующая строка вызывается из словаря 
# и впоследствии возвращается Min необходимо, так как len(names) может быть > 4

# The * in *names ensures that the list names is blown up and that format is called
# as if each item in names was passed to format individually, i. e.
# format(names[0], names[1], .... , names[n], others = length - 2
return d[min(4, length)].format(*names, others = length - 2)
