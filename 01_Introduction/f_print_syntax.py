"""
Purpose: print() function synatx and usage
"""

name = "Almighty"

print("name =", name)
print("Name of the student is name")

print("Name of the student is"+name)
print("Name of the student is "+name)
print()

print("Name of the student is", name)
print("Name of the student is", name, sep =' ')
print("Name of the student is", name, sep ='-')
print("Name of the student is", name, sep = '')
print()

print(1, 2, 3, 4, 5, 6)
print(1, 2, 3, 4, 5, 6, sep=" ")
print()

print(1, 2, 3, 4, 5, 6, sep="~")
print(1, 2, 3, 4, 5, 6, sep="_")
print(1, 2, 3, 4, 5, 6, sep=":")
print()

print("1 + int('2') =", 1 + int("2"))
print("str(1) + '2' =", str(1) + '2')
print()

print("int('234') =", int("234"))

# print("int('23.4') =", int('23.4')) # ValueError: 
# print("int('two') =", int('two)) # ValueError: 
