#Ch04 pe10
#Description: Tuition Increase - This program has a loop that display the projected semester amount for then next five years. 


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
# #Description: Tuition Increase - This program has a loop that display the projected semester amount for then next five years.


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
