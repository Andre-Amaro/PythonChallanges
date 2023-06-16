"""
Min-maxing
Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""

def largest_difference(x):
    small_num = 100
    large_num = -100
    for number in x:
        if number < small_num:
            small_num = number
        if number > large_num:
            large_num = number
  
    result = large_num - small_num
    return result
    
largest_difference([1,2,3])
