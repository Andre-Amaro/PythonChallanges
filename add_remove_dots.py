"""

Adding and removing dots
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)

"""
def add_dots(text):
    
    new_text = ''
    indice = 0

    count = 0
    while indice < len(text):
        indice += 1
        if indice == len(text):
            new_text += text[count]
            break
        new_text += text[count] + '.'
        count += 1

    return new_text
def remove_dots(text):
    new_text = ''
    
    for letra in text:
        if letra != '.':
            new_text += letra
    return new_text

    
add_dots('xx')

remove_dots('p.y.t.h.o.n.')

remove_dots(add_dots('python'))
