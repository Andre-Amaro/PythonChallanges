"""
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
"""

def is_anagram(x,y):
    anagram = False
    
    if sorted(x) == sorted(y):
        anagram = True
    else:
        anagram = False
    return anagram
    
is_anagram("abc", "cac")

# or

# def is_anagram(x,y)
#   return sorted(x) == sorted(y)
