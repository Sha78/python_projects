#Ch02 pe11
#Description: This program asks user to enter amount of male and female students and displays the percentage of them. 

registered_males = int(input("Enter the number of males registered for the class? "))
registered_females = int(input("Enter the number of females registered for the class? "))

total = registered_males + registered_females

male_percentage = registered_males/total 
female_percentage = registered_females/total

print(format(male_percentage, '.1%'),  " Is the percent of males in the class. ")
print(format(female_percentage, '.1%'), " Is the percent of females in the class. ")

#*****************************footer************************************************************
# [shaycraf@hills Ch02]$ python3 pe11.py
# Enter the number of males registered for the class? 40
# Enter the number of females registered for the class? 60
# 40.0%  Is the percent of males in the class.
# 60.0%  Is the percent of females in the class.
# [shaycraf@hills Ch02]$ cat pe11.py
# #Ch02 pe11
# #Description: This program asks user to enter amount of male and female students and displays the percentage of them.

# registered_males = int(input("Enter the number of males registered for the class? "))
# registered_females = int(input("Enter the number of females registered for the class? "))

# total = registered_males + registered_females

# male_percentage = registered_males/total
# female_percentage = registered_females/total

# print(format(male_percentage, '.1%'),  " Is the percent of males in the class. ")
# print(format(female_percentage, '.1%'), " Is the percent of females in the class. ")





# [shaycraf@hills Ch02]$





