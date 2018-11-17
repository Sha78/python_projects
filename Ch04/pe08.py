#Ch04 pe08
#Description: Sum of numbers - This program asks user to enter a series of positive numbers and a negative number to end the program
#Once the program ends it prints the sum of the positive numbers. 

print('Enter a series of positive numbers. Enter a negative number to end the program.')

positive_numbers = float(input('Enter a number: '))
positive_numbers_sum = 0
while positive_numbers>-1:
    positive_numbers_sum += positive_numbers
    positive_numbers = float(input('Enter a number: '))
 
print('The sum of the positive numbers you entered is: ',format(positive_numbers_sum, '.2f'))

#**********************footer for Ch04 pe08**************************************************************************
# [shaycraf@hills Ch04]$ python3 pe08.py
# Enter a series of positive numbers. Enter a negative number to end the program.
# Enter a number: 2
# Enter a number: 3
# Enter a number: 5
# Enter a number: 19
# Enter a number: 1
# Enter a number: -56
# The sum of the positive numbers you entered is:  30.00
# [shaycraf@hills Ch04]$ python3 pe08.py
# Enter a series of positive numbers. Enter a negative number to end the program.
# Enter a number: 1.2
# Enter a number: 2.3
# Enter a number: .5
# Enter a number: 19
# Enter a number: -99
# The sum of the positive numbers you entered is:  23.00
# [shaycraf@hills Ch04]$ cat pe08.py
# #Ch04 pe08
# #Description: Sum of numbers - This program asks user to enter a series of positive numbers and a negative number to end the program
# #Once the program ends it prints the sum of the positive numbers.

# print('Enter a series of positive numbers. Enter a negative number to end the program.')

# positive_numbers = float(input('Enter a number: '))
# positive_numbers_sum = 0
# while positive_numbers>-1:
#     positive_numbers_sum += positive_numbers
#     positive_numbers = float(input('Enter a number: '))

# print('The sum of the positive numbers you entered is: ',format(positive_numbers_sum, '.2f'))

#   [shaycraf@hills Ch04]$


  