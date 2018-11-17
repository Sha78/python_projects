#Ch03 pe06
#Description: This program determines if the month, day and year is magic. A date where the month times the day equals the year  
month = int(input('Enter a month in two digit numerical format: '))
day = int(input('Enter a day in two digit numerical format: '))
year = int(input('Enter a year in two digit numerical format:'))
           
           
if month * day == year:
  print('This is a Magic date !')
  
else:
  print('This is not a Magic date !')
  
#******************************footer for pe06************************************************************8
# [shaycraf@hills Ch03]$ python3 pe06.py
# Enter a month in two digit numerical format: 09
# Enter a day in two digit numerical format: 02
# Enter a year in two digit numerical format:18
# This is a Magic date !
# [shaycraf@hills Ch03]$ python3 pe06.py
# Enter a month in two digit numerical format: 03
# Enter a day in two digit numerical format: 03
# Enter a year in two digit numerical format:90
# This is not a Magic date !
# [shaycraf@hills Ch03]$

