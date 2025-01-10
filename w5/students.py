import csv

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

    with open(filename, "rt") as csv_file:
        
        read = csv.reader(csv_file)
        
        next(read)

        for row_list in read:

            key = row_list[key_column_index]

            dictionary[key] = row_list

    return dictionary

def main():
    I_number_idex = 0
    name_idex = 1

    student_dictionary = read_dictionary("C:/Users/lover/Documents/CSE 111/w5/students.csv", I_number_idex)

    inumber = input("Please Enter the I_Number (xxxxxxxxx): ")

    if inumber not in student_dictionary:
        print("No such student exists.")
    else:
        value = student_dictionary[inumber]
        name = value[name_idex]

        print(name)

if __name__ == "__main__":
    main()