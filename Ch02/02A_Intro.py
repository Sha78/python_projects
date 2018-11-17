#Assignment:  02A -intro
#Description: 
#User inputs purchase amount and the program calculates state and county tax. 

purchase_amt = float(input("Please enter the amount of purchase: $"))

state_tax = .04
county_tax = .02

print("The purchase amount is:", '$'+format(purchase_amt, '.2f'))
print("The state tax of 4% on the purchase is: ", '$'+ format(purchase_amt*state_tax, '.2f'))
print("The county tax of 2% on the purchase is: ", '$'+format(purchase_amt*county_tax, '.2f'))
print("The total combined 4% state tax and 2% county tax on the purchase is: ", '$'+format(purchase_amt*(state_tax + county_tax), '.2f'))
print("The purchase amount including 4% state and 2% county tax is: ", '$'+format(purchase_amt*(state_tax + county_tax) + purchase_amt, '.2f'))
