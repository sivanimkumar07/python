import re

try:
    title=input("enter a book title:")
    if not re.fullmatch(r"[A-Za-z]+",title):
      raise ValueError("Error:Book title must  contain only alphabets.")
    
    year=input("Enter publishing year:")
    if not re.fullmatch(r"(19|20)\d{2}", year):
        raise ValueError("Error: Publication year must be a 4-digit number starting with '19' or '20'.")
    print("\nBook details accepted!")
    print("Title:", title)
    print("Publication Year:", year)

except ValueError as e:
    print(e)

finally:
    print("\nProgram execution completed.")