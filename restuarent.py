try:
    name=input("Enter your name:")
    feedback=input("Enter your feedback:")
    if name.strip() == "":
        raise ValueError("Error: Name cannot be empty.")

    if feedback.strip() == "":
        raise ValueError("Error: Feedback cannot be empty.")

    
    print("\nThank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)

except ValueError as e:
    print(e)

finally:
    print("\nFeedback process completed.")