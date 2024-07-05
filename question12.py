s = input("Please enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print(f"The number of vowels in the string is: {count}")
