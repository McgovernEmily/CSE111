"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("What is your age?"))

heart_rate = 220 - age

first_range = heart_rate * .65
last_range = heart_rate * .85

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {first_range:.0f} and {last_range:.0f} beats per minute")

