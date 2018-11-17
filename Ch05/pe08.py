
#In Class Intro 5B: Ch05: PE08: Paint Job Estimator
# A painting company has determined that for every 112 square feet of wall space, one gallon of paint and eight hours of labor will be required. The company charges $35.00 per hour for labor.
#Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. The program should display the following data:
#     The number of gallons of paint required
#     The hours of labor required
#     The cost of the paint
#     The labor charges
#     The total cost of the paint job

#global variables used to caluculate 
WALL_SPACE_PER_PAINT= 112/1 
WALL_SPACE_PER_LABOR= 112/8
PRICE_PER_LABOR = 35/1 

def main(): #main function
  
  #inputs 
  
  wall_space = get_wall_space() #gets data about wall speace from useer
  paint_price_per_gallon = get_paint_price()#gets paint price from user
  
  #processing
  paint_required = get_paint_required(wall_space)#
  labor_required = get_labor_required(wall_space)
  total_paint_cost = get_total_paint_cost(paint_price_per_gallon, paint_required)
  total_labor_cost = get_total_labor_cost(labor_required)
  total_cost = get_total_cost(total_paint_cost, total_labor_cost)
  
  #outputs
  display_bill(paint_required, labor_required, total_paint_cost, total_labor_cost, total_cost)
  return

def get_wall_space():
    return int(input('enter the square feet of wall space to be painted: '))
def get_paint_price():
    return int(input('enter the price of the paint per gallon: '))
def get_paint_required(wall_space):
    return wall_space / WALL_SPACE_PER_PAINT
def get_labor_required(wall_space):
    return wall_space / WALL_SPACE_PER_LABOR
def get_total_paint_cost(paint_price_per_gallon, paint_required):
    return paint_price_per_gallon * paint_required
def get_total_labor_cost(hours_labor):
    return PRICE_PER_LABOR * hours_labor
def get_total_cost(paint_cost, labor_cost):
    return paint_cost + labor_cost
def display_bill(paint_required, labor_required, total_paint_cost, total_labor_cost, total_cost):
    print( 'paint required:', format(paint_required, '.2f'), 'gallons')
    print( 'labor required:', format(labor_required, '.2f'), 'hours' )
    print( 'total paint costs:', format(total_paint_cost, '.2f'), '$USD' )
    print( 'total labor costs:', format(total_labor_cost, '.2f'), '$USD' )
    print( 'total costs:', format(total_cost, '.2f'), '$USD' )

main()
  



# #/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# area_per_gallon = 112/1 
# area_per_labor = 112/8 
# dollars_per_hour = 35/1 
# def main():
  
  
  
  
  
  
  
#   main()
  
  
# #*********************************************************************************************************************************************************************

# # #Ch5 pe07
# # #Description: This code determines seating cost based on seating catigories.User inputs how many tickets were sold from each class and the program calculates the total money 
# # #made from ticket sales.
# # #There are three seating catigories at a stadium. 
# # #Class A seats cost $20 , Class B seats cost $15, Class C seats cost $10. Write a program that asks how many tickets for each class of seats were sold, 
# # #then displays the amount of income generated from each ticket sale. 

# # def classA():

# #     return int(input("Enter class A seats sold: " )) 
# # def classB():
    
# #     return int(input("Enter class B seats sold: " )) 
# # def classC():

# #     return int(input("Enter class C seats sold: " )) 
    
# # a=classA()
# # b=classB()
# # c=classC()

# # print("The total amount of money generated from all ticket sales is: $", a*20 + b*15 +c*10)

# #***********************************************************************************************************************************************************************

# # #Ch 5 pe06
# # #Description: Calories from Fat and Carbohydrates. This code displays the colories from fat and calories from carbs. User enters grams of fat and carb consumed in a day 
# # #and the program calculates how many calories there were from them that were consumed. 

# # #cals from fat = fat grams*9
# # #cals from carbs = carb grams*4


# # def fatCals():
# #   return float(input("Enter the amount of grams of fat you consume in a day: " ))

# # def carbCals(): 
# #   return float(input("Enter the amount of grams of carbohydrates you consume in a day: " ))

# # def calcFatCals(cals):
# #   return cals*9

# # def calcCarbCals(cals):
# #   return cals*4

# # a = fatCals()
# # b = carbCals()

# # print("The amount of Calories from your daily fat consumtion is: ", calcFatCals(a))
# # print("The amount of Calories from your daily carbohydrate consumtion is: ", calcCarbCals(b))







    
    
    
    
    
    
    
    
    