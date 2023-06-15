"""
Middle letter
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".


"""

def mid(text):
    
    string_len = len(text)
    invalido = ''
    letra_mid = ' '
    
    if string_len == 1:
        letra_mid = text
        return letra_mid
    elif string_len % 2 == 1:
        for letra in range(string_len):
            if letra % 2 == 1:
                letra_mid = text[letra]
        return letra_mid
    else:
       return invalido


mid("a")
