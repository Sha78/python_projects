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
# #Description: Ocean levels -

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