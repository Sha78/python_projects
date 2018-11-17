#Ch03 pe5
#Description: This program calculates the weight from mass and has a condition that lets the user 
#know if their entry is too light or too heavy. 
mass = float(input("Enter the mass of an object in Kilograms: " ))
weight = float(mass * 9.8) 
if mass<=100:
   print("The object is too light")
elif mass>=500:
     print("The object is too heavy") 
else:
    print("The weight of that object is: ", format(weight, '.2f'), "Newtons")
    
#     *******************************************
#     [shaycraf@hills Ch03]$ python3 Pe05.py
# Enter the mass of an object in Kilograms: 120
# The weight of that object is:  1176.00 Newtons
# [shaycraf@hills Ch03]$ python3 Pe05.py
# Enter the mass of an object in Kilograms: 100The object is too light
# [shaycraf@hills Ch03]$ python3 Pe05.py
# Enter the mass of an object in Kilograms: 500
# The object is too heavy
# [shaycraf@hills Ch03]$ cat Pe05.py
# #Ch03 pe5
# #Description: This program calculates the weight from mass and has a condition that lets the user
# #know if their entry is too light or too heavy.
# mass = float(input("Enter the mass of an object in Kilograms: " ))
# weight = float(mass * 9.8)
# if mass<=100:
#    print("The object is too light")
# elif mass>=500:
#      print("The object is too heavy")
# else:
#     print("The weight of that object is: ", format(weight, '.2f'), "Newtons")[shaycraf@hills Ch03]$