import os

item=input("enter the name of item:")
if not os.path.exists("item.txt"):

    with open("item.txt", "w") as file:
        file.write(item + "\n")
else:
    with open ("item.txt","a")as file:
        file.write(item + "\n")

print("\nItems in the shop:")
with open("item.txt", "r") as file:
    for line in file:
        print(line.strip())