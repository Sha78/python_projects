#Ch02  pe10
#Description: This program asks user how many cookies they want to make and calculates the ingredients 
#needed and displays the ingredients.
def main():
  
  try:
    CUPS_SUGAR = 1.5
    BUTTER_AMOUNT = 1
    CUPS_FLOUR = 2.75
    TOTAL_COOKIES = 48

    cookie_number_desired = int(input('Enter the number of cookie(s) you want to make: '))#user input


      #This code calculates ingedient amoounts.
    if cookie_number_desired == TOTAL_COOKIES: 
      print(format(CUPS_SUGAR, '.2f'),'Cup(s) of sugar.')

    elif cookie_number_desired<TOTAL_COOKIES or cookie_number_desired>TOTAL_COOKIES:
      sugar_needed = (cookie_number_desired/TOTAL_COOKIES)*CUPS_SUGAR
      print( format(sugar_needed, '.2f'),'Cup(s) of sugar')

    if cookie_number_desired == TOTAL_COOKIES:
      print(format(BUTTER_AMOUNT,'.2f'),'Cup(s) of butter.')

    elif cookie_number_desired<TOTAL_COOKIES or cookie_number_desired>TOTAL_COOKIES:
      butter_needed = (cookie_number_desired/TOTAL_COOKIES)*BUTTER_AMOUNT
      print(format(butter_needed,'.2f'),'Cup(s) of butter.')

    if cookie_number_desired == TOTAL_COOKIES:
      print(format(CUPS_FLOUR,'.2f'),'Cup(s) of flour.')

    elif cookie_number_desired<TOTAL_COOKIES or cookie_number_desired>TOTAL_COOKIES:
      flour_needed = (cookie_number_desired/TOTAL_COOKIES)*CUPS_FLOUR
      print(format(flour_needed,'.2f'),'Cup(s) of flour.')
  except ValueError:
    print('You fucked up! Enter the number of cookies want to make with intergers only zippity!')
main()
  
  
#********************footer for ch02 pe10****************************************************************

# [shaycraf@hills Ch02]$ python3 pe10.py
# Enter the number of cookie(s) you want to make: 24
# 0.75 Cup(s) of sugar
# 0.50 Cup(s) of butter.
# 1.38 Cup(s) of flour.
# [shaycraf@hills Ch02]$ cat pe10.py
# #Ch02  pe10
# #Description: This program asks user how many cookies they want to make and calculates the ingredients
# #needed and displays the ingredients.

# CUPS_SUGAR = 1.5
# BUTTER_AMOUNT = 1
# CUPS_FLOUR = 2.75
# TOTAL_COOKIES = 48

# cookie_number_desired = int(input('Enter the number of cookie(s) you want to make: '))#user input


#   #This code calculates ingedient amoounts.
# if cookie_number_desired == TOTAL_COOKIES:
#   print(format(CUPS_SUGAR, '.2f'),'Cup(s) of sugar.')

# elif cookie_number_desired<TOTAL_COOKIES or cookie_number_desired>TOTAL_COOKIES:
#   sugar_needed = (cookie_number_desired/TOTAL_COOKIES)*CUPS_SUGAR
#   print( format(sugar_needed, '.2f'),'Cup(s) of sugar')

# if cookie_number_desired == TOTAL_COOKIES:
#   print(format(BUTTER_AMOUNT,'.2f'),'Cup(s) of butter.')

# elif cookie_number_desired<TOTAL_COOKIES or cookie_number_desired>TOTAL_COOKIES:
#   butter_needed = (cookie_number_desired/TOTAL_COOKIES)*BUTTER_AMOUNT
#   print(format(butter_needed,'.2f'),'Cup(s) of butter.')

# if cookie_number_desired == TOTAL_COOKIES:
#   print(format(CUPS_FLOUR,'.2f'),'Cup(s) of flour.')

# elif cookie_number_desired<TOTAL_COOKIES or cookie_number_desired>TOTAL_COOKIES:
#   flour_needed = (cookie_number_desired/TOTAL_COOKIES)*CUPS_FLOUR
#   print(format(flour_needed,'.2f'),'Cup(s) of flour.')


# [shaycraf@hills Ch02]$



  




  
  




