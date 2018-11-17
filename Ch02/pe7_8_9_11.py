#ch02 pe07
#Description: This program has user input miles driven and displays MPG. 

miles_driven = float(input('Enter the miles driven: '))
gallons_used = float(input('Enter the gallaons of gas used: '))

miles_per_gallon = miles_driven/gallons_used

print('The miles per gallon on this drive is: ', float(format(miles_per_gallon, '.2f')))

#*******************footer***********************************************************
# [shaycraf@hills Ch02]$ python3 pe07.py
# Enter the miles driven: 60
# Enter the gallaons of gas used: 2.5
# The miles per gallon on this drive is:  24.0
# [shaycraf@hills Ch02]$ cat pe07.py
# miles_driven = float(input('Enter the miles driven: '))
# gallons_used = float(input('Enter the gallaons of gas used: '))



# miles_per_gallon = miles_driven/gallons_used

# print('The miles per gallon on this drive is: ', float(format(miles_per_gallon, '.2f')))[shaycraf@hills Ch02]$






##########################################################################################################
##########################################################################################################
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
##############################################################################################
##############################################################################################
#Ch02 pe09
#DEscription: This program asks user to input to enter celsius temperature and converts it to fahrenheit. 
celsius = int(input("What is the temperature in Celsius:? "))

fahrenheit = (9/5)*celsius + 32

print(format(celsius, '.2f'), 'in Celsius is: ',format(fahrenheit, '.2f'), 'in Fahrenheit')

# #*******************footer***********************************
# [shaycraf@hills Ch02]$ python3 pe09.py
# What is the temperature in Celsius:? 1
# 1.00 in Celsius is:  33.80 in Fahrenheit
# [shaycraf@hills Ch02]$ cat pe09.py
# #Ch02 pe09
# #DEscription: This program asks user to input to enter celsius temperature and converts it to fahrenheit.
# celsius = int(input("What is the temperature in Celsius:? "))

# fahrenheit = (9/5)*celsius + 32

# print(format(celsius, '.2f'), 'in Celsius is: ',format(fahrenheit, '.2f'), 'in Fahrenheit')
# [shaycraf@hills Ch02]$
###############################################################################################
###############################################################################################
#Ch02 pe11
#Description: This program asks user to enter amount of male and female students and displays the percentage of them. 

registered_males = int(input("Enter the number of males registered for the class? "))
registered_females = int(input("Enter the number of females registered for the class? "))

total = registered_males + registered_females

male_percentage = registered_males/total 
female_percentage = registered_females/total

print(format(male_percentage, '.1%'),  " Is the percent of males in the class. ")
print(format(female_percentage, '.1%'), " Is the percent of females in the class. ")

#*****************************footer************************************************************
# [shaycraf@hills Ch02]$ python3 pe11.py
# Enter the number of males registered for the class? 40
# Enter the number of females registered for the class? 60
# 40.0%  Is the percent of males in the class.
# 60.0%  Is the percent of females in the class.
# [shaycraf@hills Ch02]$ cat pe11.py
# #Ch02 pe11
# #Description: This program asks user to enter amount of male and female students and displays the percentage of them.

# registered_males = int(input("Enter the number of males registered for the class? "))
# registered_females = int(input("Enter the number of females registered for the class? "))

# total = registered_males + registered_females

# male_percentage = registered_males/total
# female_percentage = registered_females/total

# print(format(male_percentage, '.1%'),  " Is the percent of males in the class. ")
# print(format(female_percentage, '.1%'), " Is the percent of females in the class. ")





# [shaycraf@hills Ch02]$







