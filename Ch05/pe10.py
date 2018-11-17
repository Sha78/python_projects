#Ch05 pe10
#Description: This program uses a function to convert feet to inches. The function acceppts a as an argument and returns the number of inches in the number of 
#feet the user puts in.

INCH_IN_FOOT =12
print("Feet to inch converter")
print("----------------------")
def main():
    number_of_feet = int(input("Enter a number of feet: "))
    feet_to_inches(number_of_feet)
   
def feet_to_inches(number_of_feet):
    number_of_inches_in_feet = INCH_IN_FOOT*number_of_feet
    print("There are", number_of_inches_in_feet, "inches in", number_of_feet, "feet.")
    return number_of_inches_in_feet   
main()

#********************************footer for Ch05 pe10********************************************************************************************
# [shaycraf@hills Ch05]$ python3 pe10.py
# Feet to inch converter
# ----------------------
# Enter a number of feet: 2
# There are 24 inches in 2 feet.
# [shaycraf@hills Ch05]$ cat pe10.py
# #Ch05 pe10
# #Description: This program uses a function to convert feet to inches. The function acceppts a as an argument and returns the number of inches in the number of
# #feet the user puts in.

# INCH_IN_FOOT =12
# print("Feet to inch converter")
# print("----------------------")
# def main():
#     number_of_feet = int(input("Enter a number of feet: "))
#     feet_to_inches(number_of_feet)

# def feet_to_inches(number_of_feet):
#     number_of_inches_in_feet = INCH_IN_FOOT*number_of_feet
#     print("There are", number_of_inches_in_feet, "inches in", number_of_feet, "feet.")
#     return number_of_inches_in_feet
# main()[shaycraf@hills Ch05]$