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
###############################################################################################################################################
#**********************************************************************************************************************************************
###############################################################################################################################################
#Ch05 pe11
#Description: This program displays two random numbers that allows the user to add. If user gets it right, user gets a congratultion message
#if the user gets it wrong, user gets a message that a correct answer should be displayed. 

import random

def quiz():
  
  
  number1 = random.randint(0,100)
  number2 = random.randint(0,100)
  
  print(number1, '+', number2, '=')
  
  answer = int(input())
  right_answer = number1 + number2
  
  if answer == right_answer:
    print(answer, "is right! Congratulations!")
  else:
    print(answer, "is incorrect. Try again, a correct answer should be displayed!")
  
quiz()

#*****************************************footer for Ch5 pe11********************************************************
# [shaycraf@hills Ch05]$ python3 pe11.py
# 58 + 78 =
# 99
# 99 is incorrect. Try again, a correct answer should be displayed!
# [shaycraf@hills Ch05]$ python3 pe11.py
# 61 + 66 =
# 127
# 127 is right! Congratulations!
# [shaycraf@hills Ch05]$ cat pe11.py
# #Ch05 pe11
# #Description: This program displays two random numbers that allows the user to add. If user gets it right, user gets a congratultion message
# #if the user gets it wrong, user gets a message that a correct answer should be displayed.

# import random

# def quiz():


#   number1 = random.randint(0,100)
#   number2 = random.randint(0,100)

#   print(number1, '+', number2, '=')

#   answer = int(input())
#   right_answer = number1 + number2

#   if answer == right_answer:
#     print(answer, "is right! Congratulations!")
#   else:
#     print(answer, "is incorrect. Try again, a correct answer should be displayed!")

# quiz()[shaycraf@hills Ch05]$

###############################################################################################################################################
#**********************************************************************************************************************************************
###############################################################################################################################################
#Ch5 pe12
#Description:This program determines the large nuber in a function. 

def main():
  
  value_one = int(input("Enter a number: "))
  value_two = int(input("Enter another number: "))
  
  if value_one>value_two:
    lager_value=value_one
    
  else:
    lager_value = value_two
    
  print(lager_value, "is the larger value.")
  
  return True
  
main()
#*******************************footer for ch5 pe12***********************************************************************
# [shaycraf@hills Ch05]$ python3 pe12.py
# Enter a number: 345
# Enter another number: 5323
# 5323 is the larger value.
# [shaycraf@hills Ch05]$ cat pe12.py
# #Ch5 pe12
# #Description:This program determines the large nuber in a function. 

# def main():

#   value_one = int(input("Enter a number: "))
#   value_two = int(input("Enter another number: "))

#   if value_one>value_two:
#     lager_value=value_one

#   else:
#     lager_value = value_two

#   print(lager_value, "is the larger value.")

#   return True

# main()

