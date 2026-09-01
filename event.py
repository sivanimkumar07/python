import math
import random

names_input=input("enter guest name (comma-seperated):")

names= [name.strip() for name in names_input.split(",")]

unique_names = list(set(names))

selected_name = random.choice(unique_names)


reversed_name = selected_name[::-1]

total_unique = len(unique_names)

rounded_sqrt=round(math.sqrt(total_unique))

print("\nSelected Name:", selected_name)
print("Reversed Name:", reversed_name)
print("Total Unique Names:", total_unique)
print("Rounded Square Root:", rounded_sqrt)
