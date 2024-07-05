num_rows = int(input("Enter the number of rows: "))
for i in range(num_rows):
     print(' ' * (num_rows - i - 1), end='')
     print('*' * (2 * i + 1))