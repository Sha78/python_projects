#Write a program that will ask the user to enter the amount of a purchase. The program should then #compute the state and county sales tax. Assume the state sales tax is 4 percent and the county sales #tax is 2 percent. The program should display the amount of the pur- chase, the state sales tax, the #county sales tax, the total sales tax, and the total of the sale (which is the sum of the amount of #purchase plus the total sales tax).

#Hint: use the value 0.02 to represent 2 percent, and 0.04 to represent 4 percent.

purchase_amt = float(input("Please enter the amount of purchase: $"))

state_tax = .04
county_tax = .02

print("The purchase amount is: $"+format(purchase_amt, '.2f'))
print("The state tax of 4% on the purchase is: $"  + format(purchase_amt*state_tax, '.2f'))
print("The county tax of 2% on the purchase is: $" +format(purchase_amt*county_tax, '.2f'))
print("The total combined 4% state tax and 2% county tax on the purchase is: $" +format(purchase_amt*(state_tax + county_tax), '.2f'))
print("The purchase amount including 4% state and 2% county tax is: $" +format(purchase_amt*(state_tax + county_tax) + purchase_amt, '.2f'))


