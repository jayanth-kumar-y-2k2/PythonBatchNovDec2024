"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A = final amount
                        P = initial principal balance
                        r = annual interest rate
                        t = time (in years)

    Compound Interest : A = P(1 + r)^t
"""
p = float(input("Initial Principal Balance: "))
r = float(input("Anuual Interest Rate     :"))
t = float(input("Time(in years)           :"))

a = p * (1 + (r/100) * t)
print("Simple Interest Final Amount       :", round(a, 2))

c = p * ((1 + (r/100)) ** t)
print("Compound Interest Final Amount     :", round(c, 2))