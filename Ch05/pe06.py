#Ch 5 pe06
#Description: Calories from Fat and Carbohydrates. This code displays the colories from fat and calories from carbs. 

#cals from fat = fat grams*9
#cals from carbs = carb grams*4


# def fatCals():
#   return float(input("Enter the amount of grams of fat you consume in a day: " ))

# def carbCals(): 
#   return float(input("Enter the amount of grams of carbohydrates you consume in a day: " ))

# def calcFatCals(cals):
#   return cals*9

# def calcCarbCals(cals):
#   return cals*4

# a = fatCals()
# b = carbCals()

# print("The amount of Calories from your daily fat consumtion is: ", calcFatCals(a))
# print("The amount of Calories from your daily carbohydrate consumtion is: ", calcCarbCals(b))

# ****************************************
# [shaycraf@hills Ch05]$ python3 pe06.py
# Enter the amount of grams of fat you consume in a day: 200
# Enter the amount of grams of carbohydrates you consume in a day: 200
# The amount of Calories from your daily fat consumtion is:  1800.0
# The amount of Calories from your daily carbohydrate consumtion is:  800.0
# [shaycraf@hills Ch05]$ cat pe06.py
# #Ch 5 pe06
# #Description: Calories from Fat and Carbohydrates. This code displays the colories from fat and calories from carbs.

# #cals from fat = fat grams*9
# #cals from carbs = carb grams*4
def main():
    calF = 9
    calC = 4
    EF = float(input('Enter daily grams of fats: '))
    EC = float(input('Ener daily grams of Carbohydrates:'))
    f = fatCal(EF,calF)
    print(format(f, '.2f'),'are calories from fats')
    c = carbCal(EC,calC)
    print( format(c, '.2f'),'are calories from carbs')
  
def fatCal(a, b):
    F = a*b
    return F

def carbCal(c,d):
    C = c*d 
    return C

main()
  

  
 






# def fatCals():
#   return float(input("Enter the amount of grams of fat you consume in a day: " ))

# def carbCals():
#   return float(input("Enter the amount of grams of carbohydrates you consume in a day: " ))

# def calcFatCals(cals):
#   return cals*9

# def calcCarbCals(cals):
#   return cals*4

# a = fatCals()
# b = carbCals()

# print("The amount of Calories from your daily fat consumtion is: ", calcFatCals(a))
# print("The amount of Calories from your daily carbohydrate consumtion is: ", calcCarbCals(b))





# [shaycraf@hills Ch05]$





