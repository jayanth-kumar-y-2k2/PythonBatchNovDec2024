"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 cms

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: compute from feet to cms
            feet to inches, then
            inches to cms conversion
Step 3: Display the results
"""
val = int(input("Enter length (in feet): "))
inches = val * 12
cms = inches * 2.54

print(val, " feet is", inches, " inches")
print(inches, " inches are ", cms, " cms")
print(val, " feet is", cms, " cms")