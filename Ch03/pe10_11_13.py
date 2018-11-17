
#ch03 pe10
#Description: This program tells user to enter, pennies, nickels, dimes, and quarters to make one dollar. 
#If the user enters enough coins to make a dollar a message congradulates then,
#if not the program lets them know if they went over or under a dollar. 


PENNY = .01
NICKEL = .05
DIME = .10
QUARTER = .25
DOLLAR = 1.00

print('\t\tMoney Counting Game')
print('____________________________________________________')
print('Enter the number of each coin that adds to a dollar.\n')

penny = int(input('Enter the number of pennies: '))
nickel = int(input('Enter the number of nickels: '))
dime = int(input('Enter the number of dimes: '))
quater = int(input('Enter the number of quarters: '))

pennies = penny*PENNY
nickels = nickel*NICKEL
dimes = dime*DIME
quarters = quater*QUARTER

total = pennies+nickels+dimes+quarters

if total == DOLLAR:
  print('Congratulations! The coins you entered added to a one dollar!')
  
elif total<DOLLAR:
  print('You entered:', format(total, '.2f'), 'that is less than a Dollar')
  
#elif total>DOLLAR:
else:
  print('You entered:', format(total, '.2f'), 'that is more than a Dollar')
  
#******************************footer for Ch03 pe10*****************************************

# [shaycraf@hills Ch03]$ python3 pe10.py
#                 Money Counting Game
# ____________________________________________________
# Enter the number of each coin that adds to a dollar.

# Enter the number of pennies: 5
# Enter the number of nickels: 4
# Enter the number of dimes: 5
# Enter the number of quarters: 1
# Congratulations! The coins you entered added to a one dollar!
# [shaycraf@hills Ch03]$ cat pe10.py
# #ch03 pe10
# #Description: This program tells user to enter, pennies, nickels, dimes, and quarters to make one dollar. If the user enters enough coins to make
# #a dollar a message congradulates then, if not the program lets them know if they went over or under a dollar.


# PENNY = .01
# NICKEL = .05
# DIME = .10
# QUARTER = .25
# DOLLAR = 1.00

# print('\t\tMoney Counting Game')
# print('____________________________________________________')
# print('Enter the number of each coin that adds to a dollar.\n')

# penny = int(input('Enter the number of pennies: '))
# nickel = int(input('Enter the number of nickels: '))
# dime = int(input('Enter the number of dimes: '))
# quater = int(input('Enter the number of quarters: '))

# pennies = penny*PENNY
# nickels = nickel*NICKEL
# dimes = dime*DIME
# quarters = quater*QUARTER

# total = pennies+nickels+dimes+quarters

# if total == DOLLAR:
#   print('Congratulations! The coins you entered added to a one dollar!')

# elif total<DOLLAR:
#   print('You entered:', format(total, '.2f'), 'that is less than a Dollar')

# #elif total>DOLLAR:
# else:
#   print('You entered:', format(total, '.2f'), 'that is more than a Dollar')



# [shaycraf@hills Ch03]$

  
#######################################################################################################
#******************************************************************************************************
#######################################################################################################

#ch03 pe11
#Description: This program asks user to enter the number of book they purchased in a month and shows 
#how many book club award points they have been awarded. 

def main():
  print('Determine how many book club award points you have from your monthly book purchases.')
  number_books = int(input('Enter the number of books you bought this month: '))
  
  if number_books <= 1:# or number_books == 1:
    print('You earned zero points!')
    
  elif number_books == 2 or number_books == 3:
    print('You earned 5 points.')
  elif number_books == 4 or number_books == 5:
    print('You earned 15 points.')
  elif number_books == 6 or number_books == 7:
    print('You earned 30 points.')
  elif number_books >= 8:
    print('You earned 60 points.')
  
main()
#*********************footer for Ch03 pe11*************************************************************

# [shaycraf@hills Ch03]$ python3 pe11.py
# Determine how many book club award points you have from your monthly book purchases.
# Enter the number of books you bought this month: 6
# You earned 30 points.
# [shaycraf@hills Ch03]$ cat pe11.py
# #ch03 pe11
# #Description: This program asks user to enter the number of book they purchased in a month and shows
# #how many book club award points they have been awarded.

# def main():
#   print('Determine how many book club award points you have from your monthly book purchases.')
#   number_books = int(input('Enter the number of books you bought this month: '))

#   if number_books <= 1:# or number_books == 1:
#     print('You earned zero points!')

#   elif number_books == 2 or number_books == 3:
#     print('You earned 5 points.')
#   elif number_books == 4 or number_books == 5:
#     print('You earned 15 points.')
#   elif number_books == 6 or number_books == 7:
#     print('You earned 30 points.')
#   elif number_books >= 8:
#     print('You earned 60 points.')

# main()[shaycraf@hills Ch03]$

#######################################################################################################
#******************************************************************************************************
#######################################################################################################
#ch03 pe13
#Description: This program asks user to enter the weight of a package and displays the shipping charge. 

def main():
  
 

  TWO_OR_LESS_LBS = 1.50
  THREE_TO_SIX_LBS = 3.00
  SEVEN_TO_TEN_LBS = 4.00
  OVER_TEN_LBS = 4.75

    package_weight = float(input('Enter the weight of package: '))

if package_weight<=2:
  print('You owe ', TWO_OR_LESS_LBS)
elif package_weight>2 and package_weight <= 6:
  print('You owe ', THREE_TO_SIX_LBS)
elif package_weight>6 and package_weight <= 10:
  print('You owe ',SEVEN_TO_TEN_LBS)
elif package_weight>10:
  print('You owe ',OVER_TEN_LBS)

    
    
main()
#**********************************Professors example*****************************************************