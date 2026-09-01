import random
import math

name_input=input("enter names of customers(comma-separated):")

names = [name.strip() for name in name_input.split(",")]


unique_names = list(set(names))


random.shuffle(unique_names)

if len(unique_names) >= 2:
    
    winners = random.sample(unique_names, 2)

    
    winner1_reversed = winners[0][::-1]
    winner2_reversed = winners[1][::-1]


    total_participants = len(unique_names)

    
    rounded_sqrt = round(math.sqrt(total_participants))

    print("\n Lucky Draw Winners ")
    print("Winner 1:", winner1_reversed)
    print("Winner 2:", winner2_reversed)
    print("Total Unique Participants:", total_participants)
    print("Rounded Square Root:", rounded_sqrt)

else:
    print("At least 2 unique participants are required for the lucky draw.")
