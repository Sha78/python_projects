#Chapter 5 pe02
#Description: This code has functions that are used to clulate state and county tax on an price of an item that the user inputs. 


def calculate_tax():
    
    state_tax = .04
    county_tax = .02
    print_it(state_tax, county_tax)
    
def print_it(state_tax, county_tax):
    purchase_amt = float(input("Please enter the amount of purchase: $"))
    
    
    print("The purchase amount is:", '$'+format(purchase_amt, '.2f'))
    print("The state tax of 4% on the purchase is: ", '$'+ format(purchase_amt*state_tax, '.2f'))
    print("The county tax of 2% on the purchase is: ", '$'+format(purchase_amt*county_tax, '.2f'))
    print("The total combined 4% state tax and 2% county tax on the purchase is: ", '$'+format(purchase_amt*(state_tax + county_tax), '.2f'))
    print("The purchase amount including 4% state and 2% county tax is: ", '$'+format(purchase_amt*(state_tax + county_tax) + purchase_amt, '.2f'))
    
calculate_tax()

#*************************************************************************************************************************
#Chapter 5 pe02
#Description: This code has functions that are used to clulate state and county tax on an price of an item that the user inputs. 
#note:this is another version of the assignment. 
def getPrice():
    return float(input("Please enter price of item: "))
    
def stateTax(price):
    return .02*price

def countyTax(price):
    return .04*price
    
def bothTax(y, x):
    both = y + x
    return both

x = getPrice()
y = stateTax(x)
z = countyTax(x)

print("The price you entered is: $", x)
print('The state tax is: $', stateTax(x))
print('The state tax is: $', countyTax(x))
print('Both state and county tax together is: $',format(bothTax(y,z), '.2f'))
print('The total including all tax is: $',format(x+bothTax(y,z), '.2f'))

#*********************************************************************************************************************

#Ch5 pe03
#Description: This program uses functions to ask user to enter the cost to replace property then returns a minimum 
#coverage of insurance (80%) 

def replacement_cost(): 
    return float(input("How much is the replacement cost of your property? "))
    
def min_insurance(cost):
    min = .8*cost
    return min
    
   
x=replacement_cost()
y =min_insurance(x)
    
print("You entered: ", x)
print("The minimum amount of insurance you should buy for your property is: ",y)


# *********************************************** ********** *****************
# [shaycraf@hills Ch05]$ python3 pe03.py
# Please enter the amount of purchase: $10
# The purchase amount is: $10.00
# The state tax of 4% on the purchase is:  $0.40
# The county tax of 2% on the purchase is:  $0.20
# The total combined 4% state tax and 2% county tax on the purchase is:  $0.60
# The purchase amount including 4% state and 2% county tax is:  $10.60
# Please enter price of item: 10
# The price you entered is: $ 10.0
# The state tax is: $ 0.2
# The state tax is: $ 0.4
# Both state and county tax together is: $ 0.60
# The total including all tax is: $ 10.60
# How much is the replacement cost of your property? 12222
# You entered:  12222.0
# The minimum amount of insurance you should buy for your property is:  9777.6
# [shaycraf@hills Ch05]$ cat pe03.py#Chapter 5 pe02
# #Description: This code has functions that are used to clulate state and county tax on an price of an item that the user inputs.

# def calculate_tax():

#     state_tax = .04
#     county_tax = .02
#     print_it(state_tax, county_tax)

# def print_it(state_tax, county_tax):
#     purchase_amt = float(input("Please enter the amount of purchase: $"))


#     print("The purchase amount is:", '$'+format(purchase_amt, '.2f'))
#     print("The state tax of 4% on the purchase is: ", '$'+ format(purchase_amt*state_tax, '.2f'))
#     print("The county tax of 2% on the purchase is: ", '$'+format(purchase_amt*county_tax, '.2f'))
#     print("The total combined 4% state tax and 2% county tax on the purchase is: ", '$'+format(purchase_amt*(state_tax + county_tax), '.2f'))
#     print("The purchase amount including 4% state and 2% county tax is: ", '$'+format(purchase_amt*(state_tax + county_tax) + purchase_amt, '.2f'))

# calculate_tax()

# #*************************************************************************************************************************
# #Chapter 5 pe02
# #Description: This code has functions that are used to clulate state and county tax on an price of an item that the user inputs.
# #note:this is another version of the assignment.
# def getPrice():
#     return float(input("Please enter price of item: "))

# def stateTax(price):
#     return .02*price

# def countyTax(price):
#     return .04*price

# def bothTax(y, x):
#     both = y + x
#     return both

# x = getPrice()
# y = stateTax(x)
# z = countyTax(x)

# print("The price you entered is: $", x)
# print('The state tax is: $', stateTax(x))
# print('The state tax is: $', countyTax(x))
# print('Both state and county tax together is: $',format(bothTax(y,z), '.2f'))
# print('The total including all tax is: $',format(x+bothTax(y,z), '.2f'))

# #*********************************************************************************************************************

# #Ch5 pe03
# #Description: This program uses functions to ask user to enter the cost to replace property then returns a minimum
# #coverage of insurance (80%)

# def replacement_cost():
#     return float(input("How much is the replacement cost of your property? "))

# def min_insurance(cost):
#     min = .8*cost
#     return min


# x=replacement_cost()
# y =min_insurance(x)

# print("You entered: ", x)
# print("The minimum amount of insurance you should buy for your property is: ",y)



# [shaycraf@hills Ch05]$
    


