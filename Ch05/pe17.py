#ch05 pe17
#Description: This program checks if a number is prime or not. 
def main():
    user_number = int(input("Enter a number: ")) 
    if is_prime(user_number):
      print(user_number, 'is prime')
    else: 
      print(user_number, 'is not prime')
  
    return True
def is_prime(user_number):
  answer = True
  for number in range(2, user_number//2 +1):
      if user_number % number ==0:
        answer = False
  return answer
main()
#**************************************footer for Ch5 pe17************************************************************************************
# [shaycraf@hills Ch05]$ python3 pe17.py
# Enter a number: 11
# 11 is prime
# [shaycraf@hills Ch05]$ python3 pe17.py
# Enter a number: 16
# 16 is not prime
# [shaycraf@hills Ch05]$ cat pe17.py
# #ch05 pe17
# #Description: This program checks if a number is prime or not.
# def main():
#     user_number = int(input("Enter a number: "))
#     if is_prime(user_number):
#       print(user_number, 'is prime')
#     else:
#       print(user_number, 'is not prime')

#     return True
# def is_prime(user_number):
#   answer = True
#   for number in range(2, user_number//2 +1):
#       if user_number % number ==0:
#         answer = False
#   return answer
# main()[shaycraf@hills Ch05]$