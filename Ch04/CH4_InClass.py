
#Ch4 Pe01 part 1
#Description: This code calculates how many bugs were collected in 5 days.
 
total = 0
 
for day in [1,2,3,4,5]:
   
   
   total_bugs = int(input("How many bugs were collected today: "))
   
   
   total += total_bugs
   
print("You collected", total, "bugs in 5 days.")

#************************************************************************************************

#Ch4 Pe01 part 2
#Description: This code calculates how many bugs were collected in 5 day. This uses the range function with a for loop. 

total = 0
 
for day in range(1,6):
   
   
   total_bugs = int(input("How many bugs were collected today: "))
   
   
   total += total_bugs
   
print("You collected", total, "bugs in 5 days.")

#*********************************************************************************************
#Ch4 Pe02
# Description: This code calculates how many calories were burned in 5 minuet intervals from 10 to 30.

cal_per_min = 4.2

print("On a this tredmill you burn 4.5 calories per minuets so: ")

for cals in range(10,35,5):
 
    print("In", cals,"Minuets you burned", int(cal_per_min*cals), "Calories.")
  
#********************************************************************************************
   
#Ch4 Pe03
#Description: This code has a user enter a monthly budget and calculates how much money was spent a month and a displays results. 

monthly_buget = float(input('Enter your monthly budget : '))

running_total = 0

expense = float(input('Enter an expense (0 when done ):'))
running_total = expense

while expense !=0:
  expense = float(input('Enter an expense (0 when done ):'))
  running_total += expense
  
balance = monthly_buget - running_total
  
print("Your difference is ", monthly_buget-running_total)

if(balance<0):
  print('You went over budget by $', balance -1*balance)
  
else:
  print('You went underbudget by $', balance)
  
 #*****************************************************************************************************************
#Ch4 Pe03
#Description: This is another version of Pe03

monthly_buget = float(input('Enter your monthly budget : '))

running_total = 0

expense = float(input('Enter an expense (0 when done ):'))
running_total = expense

while expense !=0:
  expense = float(input('Enter an expense (0 when done ):'))
  running_total += expense
  
balance = monthly_buget - running_total
  
print("The total expenses you had are: $", running_total)
print('Your balance after expenses is: $', balance)

#***************************************************************************************************************
#Ch4 pe04
#Description: This code inputs speed and hours and displays distance traveled.Description.


speed = int(input("speed: "))
time = int(input("hours: "))

print('\n'"Hour" '\t''\t' "Distance Traveled")
print("---------------------------------")


for hour in range(1,time+1):
    dist = speed*hour
    print(hour, '\t''\t''\t', dist)




#****************************************************************************************************************

#Ch4 pe05
#Description: This code calculates the average rainfall. 


total_rain = 0 
num_years = int(input("Enter number of years: "))

for years in range(num_years):
    for months in range(12):
        inches_per_month = int(input("Enter amount of inches of rain each month: "))
        total_rain += inches_per_month
        months = num_years*12
        
print("The number of total months are: ", months)
print("Total inches of rain for this period: ", total_rain)
print("Average rain fall for this period is: ", float(total_rain/months))

#*************************************************************************************************************
#Ch4 Pe06 
#Description: This code converts Celcius to Farenheit. 

cel = 0 

print("Celcius" '\t''\t' "Farenheit")
print("-----------------------------")

for cel in range(0,21):
    far = (9/5*cel)+32
    print(cel, '\t''\t''\t', format(far, '.02f'))
#***************************************************************************************************************
   
   
   
   
   
    
 
    
  
   
   
   
   
   
    
 
    
  

  
  





