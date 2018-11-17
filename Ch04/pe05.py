#Ch04 pe05
#This calculates annual rainfall 
total_rain = 0 
num_years = int(input("Enter number of years: "))

for years in range(num_years):
    for months in range(12):
        inches_per_month = int(input("Enter amount of inches of rain each month: "))
        
        total_rain += inches_per_month
        months = num_years*12
print("The number of total months are: ", months)
print("Total inches of rain for this period: ", total_rain)
print("Average rain fall for this period is: ", float(format(total_rain/months,'.2f')))

******************************************************
# [shaycraf@hills Ch04]$ python3 pe05.py
# Enter number of years: 1
# Enter amount of inches of rain each month: 6
# Enter amount of inches of rain each month: 5
# Enter amount of inches of rain each month: 6
# Enter amount of inches of rain each month: 5
# Enter amount of inches of rain each month: 5
# Enter amount of inches of rain each month: 5
# Enter amount of inches of rain each month: 2
# Enter amount of inches of rain each month: 5
# Enter amount of inches of rain each month: 54
# Enter amount of inches of rain each month: 4
# Enter amount of inches of rain each month: 4
# Enter amount of inches of rain each month: 44
# The number of total months are:  12
# Total inches of rain for this period:  145
# Average rain fall for this period is:  12.08
# [shaycraf@hills Ch04]$ cat pe05.py
# #Ch04 pe05
# #This calculates annual rainfall
# total_rain = 0
# num_years = int(input("Enter number of years: "))

# for years in range(num_years):
#     for months in range(12):
#         inches_per_month = int(input("Enter amount of inches of rain each month: "))

#         total_rain += inches_per_month
#         months = num_years*12
# print("The number of total months are: ", months)
# print("Total inches of rain for this period: ", total_rain)
# print("Average rain fall for this period is: ", float(format(total_rain/months,'.2f')))[shaycraf@hills Ch04]$