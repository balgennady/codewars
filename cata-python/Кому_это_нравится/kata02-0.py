'''
    https://www.codewars.com/kata/5266876b8f4bf2da9b000362/solutions/python
    Вы, вероятно, знаете систему «лайков» из Facebook и других страниц.
    Люди могут «любить» сообщения в блоге, фотографии или другие предметы. 
    Мы хотим создать текст, который должен отображаться рядом с таким элементом.

    Implement a function likes :: [String] -> String, 
    который должен принимать во входном массиве, содержащем имена людей, которым нравится элемент.

    Для 4 или более имен число в и 2 других просто увеличивается.
'''

likes1 = [] # должно быть "no one likes this"
likes2 = ["Peter"] # должно быть "Peter likes this"
likes3 = ["Jacob", "Alex"] # должно быть "Jacob and Alex like this"
likes4 = ["Max", "John", "Mark"] # должно быть "Max, John and Mark like this"
likes5 = ["Alex", "Jacob", "Mark", "Max"] # должно быть "Alex, Jacob and 2 others like this"

phrase1 = "no one"
phrase2 = " likes this"
phrase3 = " like this"
phrase4 = " others"

def likes(names):

    l = len(names)
    
    if l == 0 :
        return phrase1 + phrase2
    elif l == 1 :
        return names[0] + phrase2
    elif l == 2:
        return names[0] + " and " + names[1] + phrase3
    elif l == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + phrase3
    else:
        return names[0] + ", " + names[1] + " and " + str(len(names)-2) + phrase4 + phrase3
        

likes(likes1)
# print( likes4.index("John") ) 
# print( len(likes4) ) 
# print(likes4)
