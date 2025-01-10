# Importing math module and datetime.
import math
from datetime import date

# Finding the date for today.
current_date_and_time = date.today()
formatted_date = current_date_and_time.strftime("%Y-%m-%d")

# Inputs asking the user the info of the tire.
width_tire = int(input("Please enter the width of your tire in mm: "))
aspect_ratio_tire = int(input("Please enter the aspect ratio of the tire: "))
diameter_tire = int(input("Please enter the diameter of the wheel in inches: "))

# Calculating the formula to find volume in the tire.
volume = (math.pi * width_tire**2 * aspect_ratio_tire * 
          (width_tire * aspect_ratio_tire + 2540 * diameter_tire)) / 10000000000

# Print the calculation to the user.
print()
print(f"The approximate volume is {round(volume, 2)} liters.")\

# Asking the user if they would like to buy tires.
buy_tires = input("Would you like to buy some tires (yes or no)? ")

# Using an if statement to decide if the user should give a phone number or not through buy_tires input.
if buy_tires == 'yes':
    phone_number = input("Please enter your phone number: ")
    print("Thank you have a wonderful day! You will be contacted shortly.")
    data = f"{formatted_date}, {width_tire}, {aspect_ratio_tire}, {diameter_tire}, {round(volume, 2)}, phone number: {phone_number}"
else:
    print("Alrighty, have a fantastic day.")
    data = f"{formatted_date}, {width_tire}, {aspect_ratio_tire}, {diameter_tire}, {round(volume, 2)}"
        
# Opening the file and appending the data to the file.
with open('C:/Users/lover/Documents/CSE 111/w1/tire_volumew1/volumes.txt', "at") as volume_file:
    print(data, file=volume_file)
