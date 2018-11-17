#Ch5 pe09
#Description: This code has ther user input the total sales in a function then calculates the state and county tax and outputs it. 


#A retail company must file a monthly sales tax report listing the total sales for the month, and the amount of state and county sales tax collected. The state sales tax
#is 
#5% and the county sales tax rate is 2.5%. Write a program that asks the user to enter the total sales for the month. From this figure, 
#the application should calculate and display
#the following. *The amount of county sales tax 
#The amount of state sales tax 
#The total sales tax(Plus county tax). 

def get_total_sales_for_month():
    return int(input("Enter total sales for the month: "))
    

a = get_total_sales_for_month()
state_tax = a*.05
county_tax = a*.025
total = state_tax + county_tax 

#print(format(a, '.2f'))
print("The State tax is: ",format( state_tax, '.2f'))
print("The County tax is: ",format(county_tax, '.2f'))
print("State and County tax combined is: ", format(total, '.2f'))

#***********************************************************************************************************
#Ch5 pe09
#Description: This code calculates state tax, county tax from sales and also prints the total tax. This is another version of ch5 pe09. 
def get_total_sales_for_month():
    return int(input("Enter total sales for the month: "))

def calStateTax(sales):
    return sales * 0.05
    
def calCountyTax(sales):
    return sales * 0.025

def calTotal(sales):
    return calStateTax(sales) + calCountyTax(sales)

a = get_total_sales_for_month()
total = calTotal(a)


#state_tax = a*.05
#county_tax = a*.025
#total = state_tax + county_tax 


print("The State tax is: ",format( calStateTax(a), '.2f'))
print("The County tax is: ",format(calCountyTax(a), '.2f'))
print("State and County tax combined is: ", format(total, '.2f'))

# #/////////////////////////////////
# [shaycraf@hills Ch05]$ python3 pe09.py
# Enter total sales for the month: 100
# The State tax is:  5.00
# The County tax is:  2.50
# State and County tax combined is:  7.50
# Enter total sales for the month: 100
# The State tax is:  5.00
# The County tax is:  2.50
# State and County tax combined is:  7.50
# [shaycraf@hills Ch05]$ cat pe09.py
# #Ch5 pe09
# #Description: This code has ther user input the total sales in a function then calculates the state and county tax and outputs it.


# #A retail company must file a monthly sales tax report listing the total sales for the month, and the amount of state and county sales tax collected. The state sales tax
# #is
# #5% and the county sales tax rate is 2.5%. Write a program that asks the user to enter the total sales for the month. From this figure,
# #the application should calculate and display
# #the following. *The amount of county sales tax
# #The amount of state sales tax
# #The total sales tax(Plus county tax).

# def get_total_sales_for_month():
#     return int(input("Enter total sales for the month: "))


# a = get_total_sales_for_month()
# state_tax = a*.05
# county_tax = a*.025
# total = state_tax + county_tax

# #print(format(a, '.2f'))
# print("The State tax is: ",format( state_tax, '.2f'))
# print("The County tax is: ",format(county_tax, '.2f'))
# print("State and County tax combined is: ", format(total, '.2f'))

# #***********************************************************************************************************
# #Ch5 pe09
# #Description: This code calculates state tax, county tax from sales and also prints the total tax. This is another version of ch5 pe09.
# def get_total_sales_for_month():
#     return int(input("Enter total sales for the month: "))

# def calStateTax(sales):
#     return sales * 0.05

# def calCountyTax(sales):
#     return sales * 0.025

# def calTotal(sales):
#     return calStateTax(sales) + calCountyTax(sales)

# a = get_total_sales_for_month()
# total = calTotal(a)


# #state_tax = a*.05
# #county_tax = a*.025
# #total = state_tax + county_tax


# print("The State tax is: ",format( calStateTax(a), '.2f'))
# print("The County tax is: ",format(calCountyTax(a), '.2f'))
# print("State and County tax combined is: ", format(total, '.2f'))






# [shaycraf@hills Ch05]$






