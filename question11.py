name = input("Please enter your name: ")
age_input = input("Please enter your age (press Enter to skip): ")
age = int(age_input) if age_input else 25
print(f"Hello, {name}! You are {age} years old.")
