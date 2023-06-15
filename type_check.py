"""
Type check
Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

"""


def only_ints(x,y):
    
    x_type = type(x)
    y_type = type(y)
    
    if x_type == y_type:
        return True
    else:
        return False
    
    
only_ints(1,1)
