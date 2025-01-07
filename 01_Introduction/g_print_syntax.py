"""
Purpose: print() function syntax and usage
    Escape Sequences
        - character whose presence is felt, but they were not printed
        \t - tab space
        \n - new line
        \b - overwrites previous character

        r'' - raw string

"""

print("hello world python")
print("hello \tworld \tpython")
print("hello \tworld \npython")


print()

# To ignore the escape sequences
print("hello \tworld \\npython")
print(r"hello \tworld \npython")

print("C:\my\newfolder")
print(r"C:\my\newfolder")
print()



# -------------------
# print(data, sep=" ", end = '\n)

print("hello") # default end = '\n'
print("world")


print("hello", end ='\n')
print("world", end = '\n')

print("hello", end = "____")
print("world")


print("hello", end = '\t')
print("world")


print("hello", "python", 12132, end = '\t')
print("world")

print("hello", "python", 12132, end = '\t', sep =';')
print("world")