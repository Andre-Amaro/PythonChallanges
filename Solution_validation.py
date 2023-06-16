"""
Challenge
Solution validation
The aim of this challenge is to write code that can analyze code submissions. We'll simplify things a lot to not make this too hard.

Write a function named validate that takes code represented as a string as its only parameter.

Your function should check a few things:

the code must contain the def keyword
otherwise return "missing def"
the code must contain the : symbol
otherwise return "missing :"
the code must contain ( and ) for the parameter list
otherwise return "missing paren"
the code must not contain ()
otherwise return "missing param"
the code must contain four spaces for indentation
otherwise return "missing indent"
the code must contain validate
otherwise return "wrong name"
the code must contain a return statement
otherwise return "missing return"
If all these conditions are satisfied, your code should return True.

Here comes the twist: your solution must return True when validating itself.
"""
code = "ddef(x)os:"

def validate(code_text):
    
    missing_indent = 'missing indent'
    missing_def = 'missing def'
    missing_end = 'missing :'
    missing_paren = 'missing paren'
    missing_param = 'missing param'
    missing_return = 'missing return'
    wrong_name = 'wrong name'

    param = "("
    if "def" not in code_text:
        return missing_def
    elif ":" not in code_text:
        return missing_end
    elif "(" not in code_text and ")" not in code_text:
        return missing_paren
    elif param +")" in code_text:
        return missing_param
    elif "    " not in code_text:
        return missing_indent
    elif 'validate' not in code_text:
        return wrong_name
    elif 'return' not in code_text:
        return missing_return
    else:
        return True
        
validate(code)    
