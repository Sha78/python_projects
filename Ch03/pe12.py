#Ch03 pe12
#Description: This program asks user to enter the number of packages purachased. The program displays the discount and the total amount of the purchase after the discount. 
#Packages sell for 99 dollars. 


#Quantity  ------- Discount
#--------------------------
#10 - 19                10%
#20 - 49                20%
#50 - 99                30%
#100 or more            40%


PACKAGE_PRICE = 99

QUANTITY_OF_TEN_TO_NINETEEN = 10
QUANTITY_OF_TWENTY_TO_FOURTYNINE = 20
QUANTITY_OF_FIFTY_TO_NINETYNINE = 50
QUANTITY_OF_ONEHUNDRED_UP = 100

TEN_PERCENT = .1
TWENTY_PERCENT= .2
THIRTY_PERCENT = .3
FOURTY_PERCENT= .4



number_of_packages_purchased = int(input('Enter the number of packages purchased: '))

gross_amount = number_of_packages_purchased*PACKAGE_PRICE

ten_percent_discount = gross_amount*TEN_PERCENT
twenty_percent_discount = gross_amount*TWENTY_PERCENT
thirty_percent_discount = gross_amount*THIRTY_PERCENT
fourty_percent_discount = gross_amount*FOURTY_PERCENT

after_discount_one =  gross_amount - (gross_amount*TEN_PERCENT)
after_discount_two =  gross_amount - (gross_amount*TWENTY_PERCENT)
after_discount_three =  gross_amount - (gross_amount*THIRTY_PERCENT)
after_discount_four =  gross_amount - (gross_amount*FOURTY_PERCENT)

if number_of_packages_purchased >= QUANTITY_OF_TEN_TO_NINETEEN and number_of_packages_purchased < QUANTITY_OF_TWENTY_TO_FOURTYNINE:
  print('The discount for your purchase is: $',format(ten_percent_discount, '.2f'))
  print('The cost of your purchase after a 10% discount is: $',format(after_discount_one, '.2f'))
  
elif number_of_packages_purchased >=QUANTITY_OF_TWENTY_TO_FOURTYNINE and number_of_packages_purchased < QUANTITY_OF_FIFTY_TO_NINETYNINE:
  print('The discount for your purchase is: $',format(twenty_percent_discount, '.2f'))
  print('The cost of your purchase after a 20% discount is: $',format(after_discount_two, '.2f'))
  
elif number_of_packages_purchased >=QUANTITY_OF_FIFTY_TO_NINETYNINE and number_of_packages_purchased < QUANTITY_OF_ONEHUNDRED_UP:
  print('The discount for your purchase is: $',format(thirty_percent_discount, '.2f'))
  print('The cost of your purchase after a 30% discount is: $',format(after_discount_three, '.2f'))
  
elif number_of_packages_purchased >=QUANTITY_OF_ONEHUNDRED_UP:
  print('The discount for your purchase is: $',format(fourty_percent_discount, '.2f'))
  print('The cost of your purchase after a 40% discount is: $',format(after_discount_four, '.2f'))
  
else:
  print('No discount for you!')
  print('You only purchased:', number_of_packages_purchased, 'packages. Your total is: $', format(gross_amount, '.2f'))
  
#**********************************************                    ******************************************************************  
#**********************************************Footer for Ch03 pe12******************************************************************
#**********************************************                    ******************************************************************


# [shaycraf@hills Ch03]$ python3 pe12.py
# Enter the number of packages purchased: 1
# No discount for you!
# You only purchased: 1 packages. Your total is: $ 99.00
# [shaycraf@hills Ch03]$ python3 pe12.py
# Enter the number of packages purchased: 10
# The discount for your purchase is: $ 99.00
# The cost of your purchase after a 10% discount is: $ 891.00
# [shaycraf@hills Ch03]$ python3 pe12.py
# Enter the number of packages purchased: 20
# The discount for your purchase is: $ 396.00
# The cost of your purchase after a 20% discount is: $ 1584.00
# [shaycraf@hills Ch03]$ python3 pe12.py
# Enter the number of packages purchased: 50
# The discount for your purchase is: $ 1485.00
# The cost of your purchase after a 30% discount is: $ 3465.00
# [shaycraf@hills Ch03]$ python3 pe12.py
# Enter the number of packages purchased: 100
# The discount for your purchase is: $ 3960.00
# The cost of your purchase after a 40% discount is: $ 5940.00
# [shaycraf@hills Ch03]$ cat pe12.py
# #Ch03 pe12
# #Description: This program asks user to enter the number of packages purachased. The program displays the discount and the total amount of the purchase after the discount.
# #Packages sell for 99 dollars.


# #Quantity  ------- Discount
# #--------------------------
# #10 - 19                10%
# #20 - 49                20%
# #50 - 99                30%
# #100 or more            40%


# PACKAGE_PRICE = 99

# QUANTITY_OF_TEN_TO_NINETEEN = 10
# QUANTITY_OF_TWENTY_TO_FOURTYNINE = 20
# QUANTITY_OF_FIFTY_TO_NINETYNINE = 50
# QUANTITY_OF_ONEHUNDRED_UP = 100

# TEN_PERCENT = .1
# TWENTY_PERCENT= .2
# THIRTY_PERCENT = .3
# FOURTY_PERCENT= .4



# number_of_packages_purchased = int(input('Enter the number of packages purchased: '))

# gross_amount = number_of_packages_purchased*PACKAGE_PRICE

# ten_percent_discount = gross_amount*TEN_PERCENT
# twenty_percent_discount = gross_amount*TWENTY_PERCENT
# thirty_percent_discount = gross_amount*THIRTY_PERCENT
# fourty_percent_discount = gross_amount*FOURTY_PERCENT

# after_discount_one =  gross_amount - (gross_amount*TEN_PERCENT)
# after_discount_two =  gross_amount - (gross_amount*TWENTY_PERCENT)
# after_discount_three =  gross_amount - (gross_amount*THIRTY_PERCENT)
# after_discount_four =  gross_amount - (gross_amount*FOURTY_PERCENT)

# if number_of_packages_purchased >= QUANTITY_OF_TEN_TO_NINETEEN and number_of_packages_purchased < QUANTITY_OF_TWENTY_TO_FOURTYNINE:
#   print('The discount for your purchase is: $',format(ten_percent_discount, '.2f'))
#   print('The cost of your purchase after a 10% discount is: $',format(after_discount_one, '.2f'))

# elif number_of_packages_purchased >=QUANTITY_OF_TWENTY_TO_FOURTYNINE and number_of_packages_purchased < QUANTITY_OF_FIFTY_TO_NINETYNINE:
#   print('The discount for your purchase is: $',format(twenty_percent_discount, '.2f'))
#   print('The cost of your purchase after a 20% discount is: $',format(after_discount_two, '.2f'))

# elif number_of_packages_purchased >=QUANTITY_OF_FIFTY_TO_NINETYNINE and number_of_packages_purchased < QUANTITY_OF_ONEHUNDRED_UP:
#   print('The discount for your purchase is: $',format(thirty_percent_discount, '.2f'))
#   print('The cost of your purchase after a 30% discount is: $',format(after_discount_three, '.2f'))

# elif number_of_packages_purchased >=QUANTITY_OF_ONEHUNDRED_UP:
#   print('The discount for your purchase is: $',format(fourty_percent_discount, '.2f'))
#   print('The cost of your purchase after a 40% discount is: $',format(after_discount_four, '.2f'))

# else:
#   print('No discount for you!')
#   print('You only purchased:', number_of_packages_purchased, 'packages. Your total is: $', format(gross_amount, '.2f'))




# [shaycraf@hills Ch03]$
 

    



