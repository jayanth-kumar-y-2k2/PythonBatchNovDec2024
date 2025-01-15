"""
Purpose: WAP to display the multiplication table from 10 to 1, for the first 10 tables
1 * 10 = 10
1 * 9  =  9
...

10 * 10 = 100
10 *  9 =  90
10 *  8 =  80
10 *  7 =  70
10 *  6 =  60
10 *  5 =  50
10 *  4 =  40
10 *  3 =  30
10 *  2 =  20
10 *  1 =  10
"""

LIMIT = 10
i = 1

while i <= LIMIT:
    j = LIMIT
    while j>0:
        print(f"{i:2} * {j:2} = {i*j:3}")
        j -= 1
    i += 1
    print("="*15)
