"""
Purpose: Python is a dynamic typed language
    Programming Languages
        - Classification
            1. Static-Typed Languages
                - first declare the variables, &
                - then use them
                    int a, float b # Declaration
                    a = 10 #Initialization
            
            2. Dynamic Typed Languages
                - create when needed, no declaration required
                    num = 123
                - line or block based execution

    python code -> python byte code -> python interpreter -> C compiler -> machine level
    So, python is slower compared to other compiler based languages.

"""

num1 = 100
print(num1)

print("num1")

print("num1", num1)

print("num1 =", num1)

print("num1 =", num1,"type =", type(num1))

num1 = 300
print("num1 =", num1,"type =", type(num1))

num1 = 300.0 #float
print("num1 =", num1,"type =", type(num1)) 

num1 = 300. #float
print("num1 =", num1,"type =", type(num1))

num1 = 300, #tuple
print("num1 =", num1,"type =", type(num1))

num1 = (300,) #tuple
print("num1 =", num1,"type =", type(num1))

num1 = -0.09 #float
print("num1 =", num1,"type =", type(num1))

num1 = -0.09j #complex numbers
print("num1 =", num1,"type =", type(num1))

num1 = "300" #string
print("num1 =", num1,"type =", type(num1))

num1 = "three"
print("num1 =", num1,"type =", type(num1))

num1 = True # Boolean
print("num1 =", num1,"type =", type(num1))

num1 = None # None
print("num1 =", num1,"type =", type(num1))

num1 = "None"
print("num1 =", num1,"type =", type(num1))

