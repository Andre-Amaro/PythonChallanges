"""
Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
"""

def triple_and(x,y,z):
    
    if x and y and z:
        return True
    else:
        return False
    
triple_and(1,0,3)
