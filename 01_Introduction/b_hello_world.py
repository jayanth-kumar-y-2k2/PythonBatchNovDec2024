#!/usr/bin/python3
"""
Purpose: Basic PEP 8 guidelines
        Shebang line

    PEP - Python Enhancement Proposal
    PEP 8 - coding style guide

This is docstring

"""

print("Hello World")
print(True)
print("True",123,None)

def wishes(name):
    wish = "How are you {0}".format(name)
    print(wish)

wishes("Jayanth")