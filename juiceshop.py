import random
apple_juice = 15.5
orange_juice =10
grape_juice=10.25

total_volume= apple_juice + orange_juice + grape_juice
print("Total_volume:",total_volume)

total_int=int(total_volume)
print("integer:",total_int)

total_str=str(total_volume)
print("string:",total_str)

bonus_litter=random.randint(5,10)
final_total=total_volume + bonus_litter

print("bonus:",bonus_litter)
print("total_volume:",final_total)