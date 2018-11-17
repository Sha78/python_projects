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