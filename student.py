import os

if os.path.exists("students.txt"):
    print("Existing student names:")
    with open("students.txt", "r") as file:
        print(file.read())


count = int(input("How many student names do you want to add? "))


with open("students.txt", "a") as file:
    for i in range(count):
        name = input(f"Enter student name {i+1}: ")
        file.write(name + "\n")


print("\nUpdated student list:")
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())