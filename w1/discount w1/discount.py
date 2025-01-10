"""
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""
# Importing the datatime module to the program.
from datetime import datetime

# Asking customer for subtotal.
subtotal = float(input("Please enter the subtotal: "))

# Finding the date and day of the week.
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

# Discount rates and sales tax.
sales_tax = 0.06
discount = 0.10


# If statement figuring out if there is a discount.
if day_of_week == 1 or 2:
    if subtotal < 50:
        need_money = 50 - subtotal
        print(f"To receive the discount, add: {need_money:.2f} to your order.")

    else:
        # Finding the tax and total amount due.
        discount_total = subtotal * discount

        # Printing everything for the user.
        print(f"Discount amount: {discount_total:.2f}")
        subtotal -= discount_total

# Finding the total for sales tax.
sales_tax_total = subtotal * sales_tax
print(f"Sales tax amount: {sales_tax_total:.2f}")

# Finding the overall total for the item.
total = subtotal + sales_tax_total
print(f"Total: {total:.2f}")


