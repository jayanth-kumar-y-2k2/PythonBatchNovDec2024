"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithm:
----------
Step 1: Take a string in run-time and store in a variable
Step 2: Create a reverse string, from the given string, using string reversal
Step 3: Compare both with a condition and decide

"""

test_string = input("Enter any word: ")
print("test_string = ", test_string)

reverse_str = test_string[::-1]
print("reverse_string = ", reverse_str)

print(test_string == reverse_str)

if test_string == reverse_str:
    print(test_string, " is palindrome")
else:
    print(test_string, " is not palindrome")

another_str = input("Enter any string: ")

print("String:", another_str)

white_space_removed = another_str.replace(" ","")
print("White space removed:", white_space_removed) 

if white_space_removed == white_space_removed[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")