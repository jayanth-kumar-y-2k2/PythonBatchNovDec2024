#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithm:
============
1) is it empty 
2) is it alphabet 
3) is it vowel or not 

NOTE: handle case-sensitivity 
"""

character = input("Enter your character: ").strip()
vowels = ['a', 'e', 'i', 'o', 'u']
if character and character.isalpha():
    if character.lower() in vowels:
        print(f"{character} is a vowel")
    else:
        print(f"{character} is a consonant")
else:
    print("Enter valid character")