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

  


