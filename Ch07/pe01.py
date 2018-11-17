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


    