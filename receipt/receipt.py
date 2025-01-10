# I added an if statement making Tuesday and Wednesdays have a tax of 10% and
# while other days will have a 6% tax.

import csv
from datetime import datetime


def main():

    # Finding the date for today.
    current_date_and_time = datetime.now()
    day_of_week = current_date_and_time.weekday()

    # Creating numbered indexes.
    i_number_index = 0
    name_index = 1
    amount = 2

    try:
        # Reading the product.csv and request.csv into dictionaries.
        products_dict = read_dictionary("C:/Users/lover/Documents/CSE 111/receipt/products.csv", i_number_index)
    
        print("Walmart\n")

        # opening the request.csv.
        with open("C:/Users/lover/Documents/CSE 111/receipt/request.csv", "rt") as request_csv:
            read_request = csv.reader(request_csv)
            next(read_request)

            print("Requested Items:")

            total_items = 0
            subtotal = 0

            # Using a for loop to go through the rows in the request.csv file.
            for row_list in read_request:
                request_number = row_list[0]
                quantity = int(row_list[1])

                # Finding the requests in the product dictionary.
                product = products_dict[request_number]
                
                # Finding the name and amount in the product dictionary.
                name = product[name_index]
                amount_total = float(product[amount])

                # Printing what was requested from the dictionary.
                print(f"{name}: {quantity} @ {amount_total}")
                        
                # Total amount of items in the order.
                total_items += quantity
                        
                # The total amount of each items cost.
                subtotal += quantity * amount_total
                
            if day_of_week == 1 and 2:
                sales_tax = 0.10
                tax_amount = subtotal * sales_tax

                total_with_tax = tax_amount + subtotal

            else:
                # Finding the sales tax from the subtotal.
                sales_tax = 0.06
                tax_amount = subtotal * sales_tax

                # Incorporating the tax with the subtotal.
                total_with_tax = tax_amount + subtotal

            # Printing All the totals.
            print(f"\nThe total number of items: {total_items}")
            print(f"The subtotal is: {subtotal:.2f}")
            print(f"The tax: {tax_amount:.2f}")
            print(f"The total: {total_with_tax:.2f}")

            print("\nThank you for shopping at Walmart.")
            print(f"{current_date_and_time:%a %b %w %I:%M:%S %Y}")

    except FileNotFoundError:
            print("Error: File not Found.\n[Errno 2] No such file or directory: 'products.csv'")
    except KeyError:
        print(f"Error: unknown product ID in the request.csv file.\n'{request_number}'")
    except PermissionError:
        print("Error: Permission denied.")





def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    # Opening the file and reading it.
    with open(filename, "rt") as csv_file:
        
        read = csv.reader(csv_file)
        
        # Skipping the top row of the file.
        next(read)

        # Reading the file's rows and creating keys for them.
        for row_list in read:

            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary

if __name__ == "__main__":
    main()
