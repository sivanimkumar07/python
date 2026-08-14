grocerry=["milk","bread","eggs"]
def add_item(items):
    grocerry.append(items)
add_item("butter")    
def remove_last_item():
    if grocerry:
        grocerry.pop()

display_item = lambda items: print(f"Item: {items}")
for item in grocerry:
    display_item(item)
def count_characters(items):
    if len(items) == 0:
        return 0
    return len(items[0]) + count_characters(items[1:])

remove_last_item()
for item in grocerry:
    display_item(item)
total_chars = count_characters(grocerry)
print("Total Characters:", total_chars)
