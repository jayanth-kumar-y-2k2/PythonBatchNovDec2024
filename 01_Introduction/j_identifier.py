"""
Purpose : Identifiers in Python

    Variable
        1. Keyword --> words which have some meaning
        2. Identifer -> words which are defined 


"""
import keyword

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert',
#   'async', 'await', 'break', 'class', 'continue',
#     'def', 'del', 'elif', 'else', 'except', 
#     'finally', 'for', 'from', 'global', 'if', 
#     'import', 'in', 'is', 'lambda', 'nonlocal', 
#     'not', 'or', 'pass', 'raise', 'return', 'try',
#       'while', 'with', 'yield']

my_val = "Something"
print(my_val)

print(keyword.iskeyword("true"))
print(keyword.iskeyword("True"))
print(keyword.iskeyword("my_val"))

# Identifiers - User-defined variables
#   - Naming Convention
#     1. Keywords should not be used as identifiers
#     2. first character: a-z, A-Z, _
#     3. remaining chars: a-z, A-Z, _, 0-9

# ---- Rule 1
# True = 123        # Syntax error
# None = 'Nothing   # Syntax error

# PEP 8 - Dont create identifiers which are similar to keywords
true = 123
none = "nothing"

true_value = 123
none_result = "nothing"

# ---- Rule 2 & 3
name = "Priyanka"
name_of_the_student = "Priyanka"
first_name = "Priyanka"
student_1 = "Priyanka"
class_02_a = "Python comment operations"
first________child = "Satvik"

# PEP 8 recommends to use capitals for constants
PI = 3.1416
DOZEN = 12

# $name = "Priyanka"
# name-of-student = "Priyanka"
# name of student = "Priyanka"
# 1st_name = "Priyanka"

_2nd_student = 'someone'

_job = "software development"
__role = "Production support"
____salary = 121312144

# OOP -> name mangling
# variable -> Public variable
# _variable -> Protected variable
# __variable -> Private variable

# __variable__ -> Built-in functions
# Ex: __file__, __name__, __doc__, __dict__, __init__

print("__name__ =", __name__) # __main__
print("__file__ =", __file__)