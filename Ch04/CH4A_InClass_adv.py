
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
####################################################################################################################

#*******************************************************************************************************************
####################################################################################################################

#CH04 pe09
#Description: Ocean levels - This program calculates the sea level rise at 1.6 millimeters per year for 25 years. 

OCEAN_LEVEL =1.6
NEXT_25_YEARS =25
def main():
  level = 0
  for year in range(NEXT_25_YEARS):
      year += 1
      level += OCEAN_LEVEL
      print('In year:',year, 'the ocean level will be:', format(level, '.2f'), 'millimeters.')
      
  return True
main()
#***************************footer for Ch04 pe09**************************************************

# [shaycraf@hills Ch04]$ python3 pe09.py
# In year: 1 the ocean level will be: 1.60 millimeters.
# In year: 2 the ocean level will be: 3.20 millimeters.
# In year: 3 the ocean level will be: 4.80 millimeters.
# In year: 4 the ocean level will be: 6.40 millimeters.
# In year: 5 the ocean level will be: 8.00 millimeters.
# In year: 6 the ocean level will be: 9.60 millimeters.
# In year: 7 the ocean level will be: 11.20 millimeters.
# In year: 8 the ocean level will be: 12.80 millimeters.
# In year: 9 the ocean level will be: 14.40 millimeters.
# In year: 10 the ocean level will be: 16.00 millimeters.
# In year: 11 the ocean level will be: 17.60 millimeters.
# In year: 12 the ocean level will be: 19.20 millimeters.
# In year: 13 the ocean level will be: 20.80 millimeters.
# In year: 14 the ocean level will be: 22.40 millimeters.
# In year: 15 the ocean level will be: 24.00 millimeters.
# In year: 16 the ocean level will be: 25.60 millimeters.
# In year: 17 the ocean level will be: 27.20 millimeters.
# In year: 18 the ocean level will be: 28.80 millimeters.
# In year: 19 the ocean level will be: 30.40 millimeters.
# In year: 20 the ocean level will be: 32.00 millimeters.
# In year: 21 the ocean level will be: 33.60 millimeters.
# In year: 22 the ocean level will be: 35.20 millimeters.
# In year: 23 the ocean level will be: 36.80 millimeters.
# In year: 24 the ocean level will be: 38.40 millimeters.
# In year: 25 the ocean level will be: 40.00 millimeters.
# [shaycraf@hills Ch04]$ cat pe09.py
# #CH04 pe09
# #Description: Ocean levels - This program calculates the sea level rise at 1.6 millimeters per year for 25 years.

# OCEAN_LEVEL =1.6
# NEXT_25_YEARS =25
# def main():
#   level = 0
#   for year in range(NEXT_25_YEARS):
#       year += 1
#       level += OCEAN_LEVEL
#       print('In year:',year, 'the ocean level will be:', format(level, '.2f'), 'millimeters.')

#   return True
# main()[shaycraf@hills Ch04]$

##########################################################################################################
#/////////////////////////////////////////////////////////////////////////////////////////////////////////
##########################################################################################################
#Ch04 pe10
#Description: Tuition Increase - This program has a loop that display the projected semester tuition amount for then next five years. 


def main():
  TUITION_PER_YEAR = 8000
  TUITION_INCREASE_PER_YEAR = .03
  YEARS = 5
  
  tutition_increase = TUITION_PER_YEAR
  
  for year in range(YEARS):
    year += 1
    
    tutition_increase += TUITION_INCREASE_PER_YEAR*TUITION_PER_YEAR
    
    print('year',year, 'tuition is: ', format(tutition_increase, '.2f'))
    
  
  
  return True 
  
main()

#************************************footer for Ch04 pe10*******************************************************************

# [shaycraf@hills Ch04]$ python3 pe10.py
# year 1 tuition is:  8240.00
# year 2 tuition is:  8480.00
# year 3 tuition is:  8720.00
# year 4 tuition is:  8960.00
# year 5 tuition is:  9200.00
# [shaycraf@hills Ch04]$ cat pe10.py
# #Ch04 pe10
#Description: Tuition Increase - This program has a loop that display the projected semester tuition amount for then next five years. 


# def main():
#   TUITION_PER_YEAR = 8000
#   TUITION_INCREASE_PER_YEAR = .03
#   YEARS = 5

#   tutition_increase = TUITION_PER_YEAR

#   for year in range(YEARS):
#     year += 1

#     tutition_increase += TUITION_INCREASE_PER_YEAR*TUITION_PER_YEAR

#     print('year',year, 'tuition is: ', format(tutition_increase, '.2f'))



#   return True

# main()[shaycraf@hills Ch04]$
