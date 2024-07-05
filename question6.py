n = int(input("Enter your positive number: "))
flag = 0

if n <= 0 or n == 1:
    flag = 1
else:
    for i in range(2,n-1):
        if n % i == 0:
            flag = 1
            break

if flag == 0:
    print("It is a prime number")
else:
    print("It is not a prime number")
