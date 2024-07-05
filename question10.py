n = list((int,input("Enter the list of number")))
max_value = n[0]
for number in n:
    if number > max_value :
       max_value = number 
       
print("The max value in the list is :",max_value)
