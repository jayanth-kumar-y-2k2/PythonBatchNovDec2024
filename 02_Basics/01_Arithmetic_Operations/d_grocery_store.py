"""
Purpose: Grocery store

    Item        Cost
    ------------------
    Rice        10/kg
    Wheat       34/kg

Algorithm:
----------
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items from the user in run time

Note: input()
      -> to get the value in run-time
"""

# cost of items
cost_of_rice = 10 # per kg
cost_of_wheat = 34 # per kg

# Quantities of items
qty_of_rice = float(input("Enter Qty. of Rice (in kgs):"))
print("Qty of Rice :", qty_of_rice, type(qty_of_rice))

qty_of_wheat = float(input("Enter Qty. of Wheat (in kgs):"))
print("Qty of Wheat :", qty_of_wheat, type(qty_of_wheat))

# Selling Price Computation
sp_of_rice = cost_of_rice * qty_of_rice
print("Selling Price of Rice: ", sp_of_rice)

sp_of_wheat = cost_of_wheat * qty_of_wheat
print("Selling Price of Wheat: ", sp_of_wheat)

