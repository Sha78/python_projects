#Ch06 pe10
#Description:This program reads each player name and golf score as input by user then saves record in golf.txt file.
#THen another program reads the records from file and displays them. 

def main():
  
  num_golfers = (int(input('Enter number of golfers: ')))
  
  for golfers in range(num_golfers):
    file_out = open('golf.txt', 'w')
    golf_name = input('Enter name: ')
    golf_score = input('Enter score: ')

  file_out.write(golf_name + '\n')
  file_out.write(golf_score + '\n') 
  file_out.close()

file_in = open('golf.txt', 'r')
name = file_in.readline()
  
while name != '':
  score = file_in.readline()
  
  print(name.rstrip('\n'), score.rstrip('\n'))
  name = file_in.readline()
  
main()

#********************Footer**********************Footer*****************************
# Enter score: 21
# [shaycraf@hills Ch02]$ cat inClassPartB.py
# #Ch06 pe10
# #Description:This program reads each player name and golf score as input by user then saves record in golf.txt file.
# #THen another program reads the records from file and displays them.

# def main():

#   num_golfers = (int(input('Enter number of golfers: ')))

#   for golfers in range(num_golfers):
#     file_out = open('golf.txt', 'w')
#     golf_name = input('Enter name: ')
#     golf_score = input('Enter score: ')

#   file_out.write(golf_name + '\n')
#   file_out.write(golf_score + '\n')
#   file_out.close()

# file_in = open('golf.txt', 'r')
# name = file_in.readline()

# while name != '':
#   score = file_in.readline()

#   print(name.rstrip('\n'), score.rstrip('\n'))
#   name = file_in.readline()

# main()

#   [shaycraf@hills Ch02]$

#############################################################################################
#############################################################################################
#Ch 02   pe12
#Description: This program calculates and displays the transaction of the buying and selling of stocks.

TRANSACTION_COMMISSION_PRICE = .03
INITIAL_PRICE_PER_SHARE = 40
SOLD_SHARE_SALES_PRICE = 42.75
NUMBER_SHARES_BOUGHT = 2000

amount_paid = NUMBER_SHARES_BOUGHT*INITIAL_PRICE_PER_SHARE 
comission_paid_when_bought = amount_paid*TRANSACTION_COMMISSION_PRICE 
amount_received_when_sold = SOLD_SHARE_SALES_PRICE*NUMBER_SHARES_BOUGHT
comission_paid_when_sold = amount_received_when_sold*TRANSACTION_COMMISSION_PRICE
total_commision = comission_paid_when_sold + comission_paid_when_bought

money_left_after_sale_plus_commision = amount_received_when_sold - comission_paid_when_sold - amount_paid

print('\nAmount paid for stocks: $', format(amount_paid, '.2f'))
print('\nCommission paid on stocks when bought: $', format(comission_paid_when_bought, '.2f'))
print('\nGross amount received when sold stocks: $', format(amount_received_when_sold, '.2f'))
print('\nCommission paid on stocks when sold: $', format(comission_paid_when_sold, '.2f'))
print('\nProfit from stock transaction including commission fees: $',format(amount_received_when_sold -amount_paid -total_commision, '.2f'))

#***************************Footer********************************Footer**********************************
# [shaycraf@hills Ch02]$ python3 pe10.py

# Amount paid for stocks: $ 80000.00

# Commission paid on stocks when bought: $ 2400.00

# Gross amount received when sold stocks: $ 85500.00

# Commission paid on stocks when sold: $ 2565.00

# Profit from stock transaction including commission fees: $ 535.00
# [shaycraf@hills Ch02]$ cat pe10.py
# #Ch 02   pe10
# #Description: This program calculates and displays the transaction of the buying and selling of stocks.

# TRANSACTION_COMMISSION_PRICE = .03
# INITIAL_PRICE_PER_SHARE = 40
# SOLD_SHARE_SALES_PRICE = 42.75
# NUMBER_SHARES_BOUGHT = 2000

# amount_paid = NUMBER_SHARES_BOUGHT*INITIAL_PRICE_PER_SHARE
# comission_paid_when_bought = amount_paid*TRANSACTION_COMMISSION_PRICE
# amount_received_when_sold = SOLD_SHARE_SALES_PRICE*NUMBER_SHARES_BOUGHT
# comission_paid_when_sold = amount_received_when_sold*TRANSACTION_COMMISSION_PRICE
# total_commision = comission_paid_when_sold + comission_paid_when_bought

# money_left_after_sale_plus_commision = amount_received_when_sold - comission_paid_when_sold - amount_paid

# print('\nAmount paid for stocks: $', format(amount_paid, '.2f'))
# print('\nCommission paid on stocks when bought: $', format(comission_paid_when_bought, '.2f'))
# print('\nGross amount received when sold stocks: $', format(amount_received_when_sold, '.2f'))
# print('\nCommission paid on stocks when sold: $', format(comission_paid_when_sold, '.2f'))
# print('\nProfit from stock transaction including commission fees: $',format(amount_received_when_sold -amount_paid -total_commision, '.2f'))[shaycraf@hills Ch02]$
  
############################################################################################
############################################################################################
#Ch02 pe13
#Description: This program takes user input of length of a row, end-post space and space between vines 
#and calculates the number of plant that will be used. 

def main():
  
  row_length = float(input('Enter the length of the row for grapevines in feet: '))
  end_post_space = float(input('Enter the space used by end post assembly in feet: '))
  space_between_grapevines = float(input('Enter the space between vines in feet: '))
  
  
  
  number_of_grapevine_plants = (row_length - end_post_space*2)/space_between_grapevines
  
 
  
  print('The number of grapevine you can have in the row is: ', int(number_of_grapevine_plants ))
  
main()
#*****************footer******************footer for pe13.py********************************
# [shaycraf@hills Ch02]$ python3 pe13.py
# Enter the length of the row for grapevines in feet: 50
# Enter the space used by end post assembly in feet: 2
# Enter the space between vines in feet: 2
# The number of grapevine you can have in the row is:  23
# [shaycraf@hills Ch02]$ cat pe13.py
# def main():

#   row_length = float(input('Enter the length of the row for grapevines in feet: '))
#   end_post_space = float(input('Enter the space used by end post assembly in feet: '))
#   space_between_grapevines = float(input('Enter the space between vines in feet: '))



#   number_of_grapevine_plants = (row_length - end_post_space*2)/space_between_grapevines



#   print('The number of grapevine you can have in the row is: ', int(number_of_grapevine_plants ))

# main()
#   [shaycraf@hills Ch02]$





  
  
  
  
  