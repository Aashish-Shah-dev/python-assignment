def is_happy(n):
    seen = set()  
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n)) 
    return n == 1
num = int(input("Enter a number to check if it's happy: "))
if is_happy(num):
    print(f"{num} is a happy number.")
else:
    print(f"{num} is not a happy number.")
