fruits=["apple","orenge","mango"]
vegetables=["carrot","pottato","tomato"]
beverages=["water","juice","tea"]

fruits.append("kiwi")

vegetables.insert(1,"onion")

beverages.remove("tea")
inventary=["fruits","vegetables","beverages"]

print(fruits[0:2])

print(vegetables[-1:])

fruit_lengths = [len(item) for item in fruits]
print("Lengths of fruit names:", fruit_lengths)
print("water" in beverages)
first_items = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items:", first_items)
print(inventary)