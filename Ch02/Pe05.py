#Assignment:  02A -intro
#Description: P.E. 4 and 5
#Sales tax and distance

car1 = 6*70
car2 = 10*70
car3 = 15*70

print("A car traveling for 6 hrs at 70mph will go:", car1, " miles")
print("A car traveling for 10 hrs at 70mph will go:", car2, " miles")
print("A car traveling for 15 hrs at 70mph will go:", car3, " miles")

#--------------------------------------------------------------------------


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


# '''
# [shaycraf@hills Ch02]$ python3 Pe05.py
# A car traveling for 6 hrs at 70mph will go: 420  miles
# A car traveling for 10 hrs at 70mph will go: 700  miles
# A car traveling for 15 hrs at 70mph will go: 1050  miles
# What is the price for item one? 20
# What is the price for item two? 3
# What is the price for item three? 3
# What is the price for item four? 3
# What is the price for item five? 3
# The subtotal is:  32.00
# The sales tax on these items are: 2.24
# The total is:  34.24[shaycraf@hills Ch02]$ cat Pe05.py
# #Assignment:  02A -intro
# #Description: P.E. 4 and 5
# #Sales tax and distance

# car1 = 6*70
# car2 = 10*70
# car3 = 15*70

# print("A car traveling for 6 hrs at 70mph will go:", car1, " miles")
# print("A car traveling for 10 hrs at 70mph will go:", car2, " miles")
# print("A car traveling for 15 hrs at 70mph will go:", car3, " miles")

# #--------------------------------------------------------------------------


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



# # A car traveling for 6 hrs at 70mph will go: 420  miles
# # A car traveling for 10 hrs at 70mph will go: 700  miles
# # A car traveling for 15 hrs at 70mph will go: 1050  miles
# # What is the price for item one? 2
# # What is the price for item two? 2
# # What is the price for item three? 2
# # What is the price for item four? 2
# # What is the price for item five? 2
# # The subtotal is:  10.00
# # The sales tax on these items are: 0.70
# # The total is:  10.70
# [shaycraf@hills Ch02]$
#'''