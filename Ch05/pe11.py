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