#Ch7 pe02
#Desciption: This program generates lotto numbers


import random #imports random.randit from py library


lotto_nums = []#empty list

for i in range(0,7):#this loop generates lottery number 7 chars long.
    lotto_nums.append(random.randint(0,9))#This code get random numbers from 0 to 9 for lotto number
    
for nums in lotto_nums:#This loop prints the lotto number
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
#************************************************************************************
#ch7 pe01
#Description: This program asks user to enter sales everyday, 
#then uses a loop to calculate sales made for the week and displays results. 


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

