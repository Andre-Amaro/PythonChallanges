"""
Consecutive zeros
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.



"""
def consecutive_zeros(x):
    zero = 0
    outro_valor = 0
    for num in x:
        if len(x) > 1:
            if num == '0':
                zero +=1
            elif num != '0':
                if zero > outro_valor:
                    outro_valor = zero
                    zero = 0
                else:
                    zero = 0
        else:
            if num == '0':
                outro_valor += 1
                
    return outro_valor
                
consecutive_zeros('1001101000110')
    
