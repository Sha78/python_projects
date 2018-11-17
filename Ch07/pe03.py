#ch7 pe03
#Description: This code asks user to enter amount of rainfall in inches in each month then returns the total amount of rainfall, the rainfall
#average, min and max. 




rain_fall = []
months = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC",]
total_rain = 0



for month in months:
    rain_fall.append(float(input("Enter amount of rain in month in inches in " + month + ': ')))
    
for i in range(len(rain_fall)):
    total_rain += rain_fall[i]
    ave = total_rain/12

min_month = months[rain_fall.index(min(rain_fall))]
max_month = months[rain_fall.index(max(rain_fall))]

              
print("The total inches of rain this year is: ", total_rain)
print("The average inches of rain this year is: ", format(ave, '.2f'))
print("The minimum inches of rainfall was in: ",min_month)
print("The maximum inches of rainfall was in: ",max_month)




    

