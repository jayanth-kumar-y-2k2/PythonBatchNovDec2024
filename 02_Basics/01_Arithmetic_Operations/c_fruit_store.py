"""
Purpose: fruit Store

    -------------------------------------------------------------
    Items   Price      QTY                      Amount
    -------------------------------------------------------------
    Apples  12/piece   5 dozens = 5 * 12 = 60   12 * 60 = 720/-
    Mangos  34/piece   3 dozens = 3 * 12 = 36   34 * 36 = 1224/-
                                              -------------------
                                                          1944/-
                                discount    -2 %        - 38.88/-
                                              -------------------
                                                          1905.12/-
                                GST         +12.5 %     + 238.14/-
                                              -------------------
                                                          2143.26/-

Algorithm
---------
Step 1: Get the cost of the fruits into variables.
Step 2: Get the quantity of fruits into variables.
        Compute the end quantity, by substituting dozen value
Step 3: Compute the selling price to each item,
        and add them
Step 4: Compute the discount amount and subtract
        from the selling price, to create payable amount
Step 5: Calculate GST amount and add to payable amount,
        to create billable amount

"""

# constants
DOZEN = 12
DISCOUNT = 2
GST = 12.5

# cost of fruits
cost_of_apple = 12 # per piece
cost_of_mango = 34 # per piece

# quantity of fruits
qty_of_apples = 5 * DOZEN
qty_of_mangos = 3 * DOZEN

# Selling Price Computation - PEMDAS
total_sp = cost_of_apple * qty_of_apples + cost_of_mango * qty_of_mangos
print("Total Selling Price :", total_sp)

# Discount Calculation
discount_amount = (total_sp * DISCOUNT)/100
print("Discount Amount     :", discount_amount)

# Payable Amount Calculation
payable_amount = total_sp - discount_amount
print("Payable Amount     :", payable_amount)

# GST Calculation
gst_on_fruits = (payable_amount * GST)/100
print("GST on Fruits      :", gst_on_fruits)

# Billable amount calculation
billable_amount = payable_amount + gst_on_fruits
print("Billable Amount    :", billable_amount)

# round(num, no_of_digits) - function
print("Billable Amount(r) :", round(billable_amount, 2))