"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create a variable 'balance' with intial value 0
Step 2: Initial deposit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

# creating constants
balance = 0
initial_deposit = 1500
salary_credited = 3300
online_purchase = 33.33
rent = 1500

total_balance = (initial_deposit + salary_credited -  
online_purchase - rent) 

print("Initial Balance: ", balance)
print("Initial deposit: ", initial_deposit)
print("Salary Credited: ", salary_credited)
print("Online Purchase: ", online_purchase)
print("Total Balance  : ", total_balance)