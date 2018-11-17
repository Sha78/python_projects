#Ch03 pe02
# Write a program that asks user to enter projected amt of total sales, 
#display the profit that will be made from that amount.


total_sales = float(input('Enter the projected amount of total sales: '))

profit = 0.23 * total_sales

print('The profit made from', format(total_sales, '.2f'), 'is: ', format(profit, '.2f'))

# *********************
# [shaycraf@hills Ch03]$ python3 Pe02.py
# Enter the projected amount of total sales: 500
# The profit made from 500.00 is:  115.00
# [shaycraf@hills Ch03]$ cat Pe02.py
# #Ch03 pe02# Write a program that asks user to enter projected amt of total sales,
# #display the profit that will be made from that amount.


# total_sales = float(input('Enter the projected amount of total sales: '))

# profit = 0.23 * total_sales

# print('The profit made from', format(total_sales, '.2f'), 'is: ', format(profit, '.2f'))[shaycraf@hills Ch03]$
