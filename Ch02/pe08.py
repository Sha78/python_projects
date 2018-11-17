#ch02 pe08
#Discription: This program asks user to enter the price of food then caluculates tip, tax and total price. 

meal_purchase = float(input("Enter the charge for the food: "))

tip = meal_purchase *.18
tax = meal_purchase *.07
total = meal_purchase + tip + tax


print("The tip is: $", format(tip, '.2f'), '\n' "The tax is: $",format(tax, '.2f'), '\n' "The total is: $", format(total, '.2f') )
# print("The tip is : ", format(tip, '.2f'))
# print("The tip is : ", format(tax, '.2f'))
# print("The tip is : ", format(total, '.2f'))

#*********************Footer**********************************************************************
# [shaycraf@hills Ch02]$ python3 pe08.py
# Enter the charge for the food: 102.97
# The tip is: $ 18.53
# The tax is: $ 7.21
# The total is: $ 128.71
# [shaycraf@hills Ch02]$ cat pe08.py
# #ch02 pe08
# #Discription: This program asks user to enter the price of food then caluculates tip, tax and total price.

# meal_purchase = float(input("Enter the charge for the food: "))

# tip = meal_purchase *.18
# tax = meal_purchase *.07
# total = meal_purchase + tip + tax


# print("The tip is: $", format(tip, '.2f'), '\n' "The tax is: $",format(tax, '.2f'), '\n' "The total is: $", format(total, '.2f') )
# # print("The tip is : ", format(tip, '.2f'))
# # print("The tip is : ", format(tax, '.2f'))
# # print("The tip is : ", format(total, '.2f'))
# [shaycraf@hills Ch02]$
