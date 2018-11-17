#Ch02 pe03
#A coustomer in a store is purchasing 5 items. Write a program that asks for each price then displays subtotal of the sale
#The amount of sales tax, and the total. Assume sales tax is 7%

item_one = int(input('What is the price for item one? '))
item_two = int(input('What is the price for item two? '))
item_three = int(input('What is the price for item three? '))
item_four = int(input('What is the price for item four? '))
item_five = int(input('What is the price for item five? '))

subtotal = item_one + item_two + item_three + item_four + item_five
sales_tax = .07*subtotal
total = subtotal+sales_tax


print('The subtotal is: ', format(subtotal, '.2f'))
print('The sales tax on these items are:',format(sales_tax, '.2f'))
print('The total is: ', format(total, '.2f'))

#***************************************************************************************

# [shaycraf@hills Ch02]$ python3 Pe04.py
# What is the price for item one? 20
# What is the price for item two? 21
# What is the price for item three? 30
# What is the price for item four? 33
# What is the price for item five? 50
# The subtotal is:  154.00
# The sales tax on these items are: 10.78
# The total is:  164.78
# [shaycraf@hills Ch02]$ cat Pe04.py
# #Ch02 pe03
# #A coustomer in a store is purchasing 5 items. Write a program that asks for each price then displays subtotal ofthe sale
# #The amount of sales tax, and the total. Assume sales tax is 7%

# item_one = int(input('What is the price for item one? '))
# item_two = int(input('What is the price for item two? '))
# item_three = int(input('What is the price for item three? '))
# item_four = int(input('What is the price for item four? '))
# item_five = int(input('What is the price for item five? '))

# subtotal = item_one + item_two + item_three + item_four + item_five
# sales_tax = .07*subtotal
# total = subtotal+sales_tax


# print('The subtotal is: ', format(subtotal, '.2f'))
# print('The sales tax on these items are:',format(sales_tax, '.2f'))
# print('The total is: ', format(total, '.2f'))
# [shaycraf@hills Ch02]$
