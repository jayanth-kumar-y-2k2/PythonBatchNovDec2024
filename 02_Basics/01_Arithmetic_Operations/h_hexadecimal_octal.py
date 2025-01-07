"""
Purpose: Convert hexa decimal to octal and vice-versa
"""

num1 = 10
num2 = 78

hexa_num1 = hex(num1)
hexa_num2 = hex(num2)

print("Number 1          : ", num1)
print("Number 2          : ", num2)

print("Hexadecimal Num1  : ", hexa_num1)
print("Hexadecimal Num2  : ", hexa_num2)

oct_num1 = oct(num1)
oct_num2 = oct(num2)

print("Octal Num1        : ", oct_num1)
print("Octal Num2        : ", oct_num2)

print("Hexa to octal num1: ", oct(int(hexa_num1, base=16)))
print("Hexa to octal num2: ", oct(int(hexa_num2, base=16)))

print("Octal to Hexa num1: ", hex(int(oct_num1, base=8)))
print("Octal to Hexa num2: ", hex(int(oct_num2, base=8)))