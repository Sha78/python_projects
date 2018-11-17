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
################################################################################################################################
################################################################################################################################
################################################################################################################################
#Ch5 pe13
#Description: This program uses a function that accepts an object's falling time in secones as argument
#and returns the distance in meters it has fallen each second. 

def main():
  
   print("The distance an object falls per second.") 
   print("----------------------------------------")
   for time in range(1, 10 +1):
     fall = falling_distance(time)
      
     print(time,':00 second(s)', '\t', format(fall, '.2f'),'meter(s)')
      
def falling_distance(time): 
  
  distance = (1/2)*9.8*time**2

  return distance
main()
#***********************************footer for Ch5 pe13*********************************************
# [shaycraf@hills Ch05]$ python3 pe13.py
# The distance an object falls per second.
# ----------------------------------------
# 1 :00 second(s)          4.90 meter(s)
# 2 :00 second(s)          19.60 meter(s)
# 3 :00 second(s)          44.10 meter(s)
# 4 :00 second(s)          78.40 meter(s)
# 5 :00 second(s)          122.50 meter(s)
# 6 :00 second(s)          176.40 meter(s)
# 7 :00 second(s)          240.10 meter(s)
# 8 :00 second(s)          313.60 meter(s)
# 9 :00 second(s)          396.90 meter(s)
# 10 :00 second(s)         490.00 meter(s)
# [shaycraf@hills Ch05]$ cat pe13.py
# #Ch5 pe13
# #Description: This program uses a function that accepts an object's falling time in secones as argument
# #and returns the distance in meters it has fallen each second.

# def main():

#    print("The distance an object falls per second.")
#    print("----------------------------------------")
#    for time in range(1, 10 +1):
#      fall = falling_distance(time)

#      print(time,':00 second(s)', '\t', format(fall, '.2f'),'meter(s)')

# def falling_distance(time):

#   distance = (1/2)*9.8*time**2

#   return distance
# main()
# [shaycraf@hills Ch05]$



################################################################################################################################
################################################################################################################################
################################################################################################################################
#Ch05 pe14
#Description: This program uses a function that accepts an objects mass and velocity from a user and returns the amount of kenetic energy it has. 
def main():
  users_mass = float(input("Enter an object's mass: ")) 
  users_velocity = float(input("Enter a velocity: ")) 

  ke  = kenetic_energy(users_mass,users_velocity)
  
  print("The kenkenetic energy from mass",format(users_mass, '.2f'), "and velocity",format(users_velocity, '.2f'), "is: ", format(ke, '.2f'))
  
  return True
def kenetic_energy(users_mass,users_velocity):  
  kenetic_energy_solution = (1/2)*users_mass*(users_velocity**2)
 
  return kenetic_energy_solution
   
main()

#*************************************footer for ch5 pe14****************************************************************************************
# [shaycraf@hills Ch05]$ python3 pe14.py
# Enter an object's mass: 15
# Enter a velocity: 2
# The kenkenetic energy from mass 15.00 and velocity 2.00 is:  30.00
# [shaycraf@hills Ch05]$ cat pe14.py
# #Ch05 pe14
# #Description: This program uses a function that accepts an objects mass and velocity from a user and returns the amount of kenetic energy it has.
# def main():
#   users_mass = float(input("Enter an object's mass: "))
#   users_velocity = float(input("Enter a velocity: "))

#   ke  = kenetic_energy(users_mass,users_velocity)

#   print("The kenkenetic energy from mass",format(users_mass, '.2f'), "and velocity",format(users_velocity, '.2f'), "is: ", format(ke, '.2f'))

#   return True
# def kenetic_energy(users_mass,users_velocity):
#   kenetic_energy_solution = (1/2)*users_mass*(users_velocity**2)

#   return kenetic_energy_solution

#main()[shaycraf@hills Ch05]$