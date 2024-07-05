num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 + num2 == num3) and (num3-num2==num1 or num3-num1==num2):
    print("The third number is the sum of the first two numbers.")
else:
    print("The third number is not the sum of the first two numbers.")