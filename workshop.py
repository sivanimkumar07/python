web_development=["Rahul","Anu","Vivek"]
data_science=["asha","meera","rohan"]
ui_ux_design=["neha","arjun","priya"]

all_participants = [web_development, data_science, ui_ux_design]

web_development.append("Kiran")
data_science.insert(1, "Sneha")
ui_ux_design.pop()
data_science_copy = data_science.copy()
data_science.clear()
print("First two Web Development participants:",
      web_development[:2])
name_lengths = [len(name) for name in data_science_copy]
print("Lengths of names in copied Data Science list:",
      name_lengths)
asha_exists = (
    "Asha" in web_development or
    "Asha" in data_science_copy or
    "Asha" in ui_ux_design
)
print("Is Asha in any workshop list?", asha_exists)
first_participants = (
    web_development[0],
    data_science_copy[0],
    ui_ux_design[0])
print("Tuple of first participants:", first_participants)
print("\nWeb Development:", web_development)
print("Data Science (cleared):", data_science)
print("Copied Data Science:", data_science_copy)
print("UI/UX Design:", ui_ux_design)
print("All Participants:", all_participants)
