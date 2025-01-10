import math

number_items = int(input("Enter the number of items:"))
item_per_box = int(input("Enter the number of items per box:"))

boxes = math.ceil(number_items / item_per_box)

boxes()

print(f"\nFor {number_items}, packing {item_per_box}"
      f" items in each box, you will need {boxes} boxes.")