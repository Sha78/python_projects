#Ch04 pe13
#Description: This program calculates an organisms population that increases by an
#average of 30% per day with a loop and puts the output in a table. 

AVERAGE_DAILY_INCREASE =.30
DAYS_TO_MULTIPLY =10

def main():
  #Input
  starting_number_of_organisms = int(input('Enter the starting number of organisms: ')) 
  increase_of_organisms = starting_number_of_organisms
  
  #Output
  print('\nDay Approximate' , '\t', 'Population')
  print('__________________________________________')
  
  #Processing
  for day in range(1,DAYS_TO_MULTIPLY+1):
    
    #Output
      print(day, '\t''\t''\t', format(increase_of_organisms, '.2f' ))
      
      #Processing
      increase_of_organisms += AVERAGE_DAILY_INCREASE*increase_of_organisms

        
      
main()
#*********************footer for ch04 pe13************************************************

# [shaycraf@hills Ch04]$ python3 pe13.py
# Enter the starting number of organisms: 2

# Day Aproximation         Population
# __________________________________________
# 1                        2.00
# 2                        2.60
# 3                        3.38
# 4                        4.39
# 5                        5.71
# 6                        7.43
# 7                        9.65
# 8                        12.55
# 9                        16.31
# 10                       21.21
# [shaycraf@hills Ch04]$ cat pe13.py
# #Ch04 pe13
# #Description: This program calculates an organisms population that increases by an
# #average of 30% per day with a loop and puts the output in a table.

# AVERAGE_DAILY_INCREASE =.30
# DAYS_TO_MULTIPLY =10
# def main():
#   starting_number_of_organisms = int(input('Enter the starting number of organisms: '))
#   increase_of_organisms = starting_number_of_organisms
#   print('\nDay Aproximation' , '\t', 'Population')
#   print('__________________________________________')
#   for day in range(1,DAYS_TO_MULTIPLY+1):
#       print(day, '\t''\t''\t', format(increase_of_organisms, '.2f'))
#       increase_of_organisms += AVERAGE_DAILY_INCREASE*increase_of_organisms



# main()

# [shaycraf@hills Ch04]$
