= int(input("Enter an integer: "))
str_x = str(x)
if str_x == str_x[::-1]:
   print(f"{x} is a palindrome.")
else:
    print(f"{x} is not a palindrome.")