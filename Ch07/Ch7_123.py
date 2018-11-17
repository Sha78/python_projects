
#ch7 pe03
#Description: This code asks user to enter amount of rainfall in inches in each month then returns the total amount of rainfall, the rainfall
#average, min and max.

rain_fall = []
months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",]
total_rain = 0



for month in months:
    rain_fall.append(float(input("Enter amount of rain in month in inches in " + month + ': ')))

for i in range(len(rain_fall)):
    total_rain += rain_fall[i]
    ave = total_rain/12

min_month = months[rain_fall.index(min(rain_fall))]
max_month = months[rain_fall.index(max(rain_fall))]
# for rain in rain_fall:
#     min_rain, max_rain = 100, 0
#     min_month = ''
#     max_month = ''
#     if rain > max_rain:
#         max_rain = rain
#         max_month = months[rain_fall.index(max_rain)]
#     if rain < min_rain:
#         min_rain = rain
#         min_month = months[rain_fall.index(min_rain)]

print("The total inches of rain this year is: ", total_rain)
print("The average inches of rain this year is: ", format(ave, '.2f'))
print("The minimum inches of rainfall was in: ",min_month)
print("The maximum inches of rainfall was in: ",max_month)

#footer
# [shaycraf@hills Ch07]$
# [shaycraf@hills Ch07]$ python3 pe03.py
# Enter amount of rain in month in inches in JAN: 1
# Enter amount of rain in month in inches in FEB: 2
# Enter amount of rain in month in inches in MAR: 3
# Enter amount of rain in month in inches in APR: 55
# Enter amount of rain in month in inches in MAY: 99
# Enter amount of rain in month in inches in JUN: 2
# Enter amount of rain in month in inches in JUL: 3
# Enter amount of rain in month in inches in AUG: 3
# Enter amount of rain in month in inches in SEP: 3
# Enter amount of rain in month in inches in OCT: 3
# Enter amount of rain in month in inches in NOV: 3
# Enter amount of rain in month in inches in DEC: 3
# The total inches of rain this year is:  180.0
# The average inches of rain this year is:  15.00
# The minimum inches of rainfall was in:  JAN
# The maximum inches of rainfall was in:  MAY
# [shaycraf@hills Ch07]$ cat pe03.py

#*****************************************************************************************

# [shaycraf@hills Ch07]$ python3 pe02.py
# 5 3 6 2 1 2 2 [shaycraf@hills Ch07]$
# [shaycraf@hills Ch07]$ cat pe02.py
#Ch7 pe02
#Desciption: This program generates lotto numbers


import random

lotto_nums = []

for i in range(0,7):
    lotto_nums.append(random.randint(0,9))

for nums in lotto_nums:
    print(nums, end = ' ')

#Footer:
# [shaycraf@hills Ch07]$ cat  pe02.py
# #Ch7 pe02
# #Desciption: This program generates lotto numbers


# import random


# lotto_nums = []

# for i in range(0,7):
#     lotto_nums.append(random.randint(0,9))

# for nums in lotto_nums:
#     print(nums, end = ' ')

# #Footer:

# [shaycraf@hills Ch07]$ python3 pe02.py
# 5 1 6 2 0 3 3 [shaycraf@hills Ch07]$

#[shaycraf@hills Ch07]$

#*******************************************************************
#ch7 pe01
#Description: This program asks user to enter sales everyday, then uses a loop to calculate sales made for the week and displays results. 


sales = [] #Enpty list
days = ["monday: ","tuesday: ","wednesday: ","thursday: ","friday: "] #list of work week days
total_sales = 0# accumulator for total sales

for day in days: #this loop changes values in sales list in correlation to the days in days list
    sales.append(float(input("Enter sales for: " + day)))
    
for day in range(len(sales)): #this loop adds the values in the sales array with the total_sales accumulator. 
    total_sales += sales[day]
    
print('The total sales you made this week is: $',format(total_sales, '.2f'))# this prints the results


# """
# #Footer: [shaycraf@hills Ch07]$ python3 pe01.py


# Enter sales for: monday: 23
# Enter sales for: tuesday: 23
# Enter sales for: wednesday: 34
# Enter sales for: thursday: 60
# Enter sales for: friday: 19.23
# The total sales you made this week is: $ 159.23
# [shaycraf@hills Ch07]$ cat pe01.py
# #ch7 pe01
# #Description: This program asks user to enter sales everyday, then uses a loop to calculate sales made for the week and displays results. 


# sales = [] #Enpty list
# days = ["monday: ","tuesday: ","wednesday: ","thursday: ","friday: "] #list of work week days
# total_sales = 0# accumulator for total sales

# for day in days:
#     sales.append(float(input("Enter sales for: " + day)))
    
# for day in range(len(sales)):
#     total_sales += sales[day]
    
# print('The total sales you made this week is: $',format(total_sales, '.2f'))
#     [shaycraf@hills Ch07]$ 
#     """
