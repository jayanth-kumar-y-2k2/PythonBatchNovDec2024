#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
"""

temperature = input("Enter temperature: ").strip()

values = list(temperature)

num = ""
for x in values:
    if x.isdigit():
        num += x

if values[-1].lower() == 'f':
    c = (int(num) - 32) * 5 / 9
    print(f"{temperature} = {c:.2f}C")
elif values[-1].lower() == 'c':
    f = (9 * int(num))/5 + 32
    print(f"{temperature} = {f:.2f}F")
else:
    print("Enter valid temperature")
