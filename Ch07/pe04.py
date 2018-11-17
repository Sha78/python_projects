#Ch7 pe4
#Description: This code asks user to enter a series of 20 numbers the returns the total of the 
#numbers entered, the average, the lowest and highest number entered. 

nums = []#list numbers are stored in the user enters
order = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th',
'13th','14th','15th','16th','17th','18th','19th','20th',]#list that showes the order of numbers entered
total = 0#Accumulator 
print("Enter a series of 20 numbers:")

for numbers in order:#loop that fills empty nums list by user entering numbers
    nums.append(float(input('Enter the ' + numbers + ' number: ')))
    
for num in range(len(nums)):#Loop that displays the total, min, max and aveerage of the numbers entered.
    total += nums[num]
    ave = total/len(nums)
    mini = min(nums)
    maxi = max(nums)
    
print("The total of the numbers you entered are: ", total)
print("The average of the numbers you entered are: ", ave)
print("The lowest number you entered was: ", mini)
print("The highest number you entered was: ", maxi)

#Footer:*****************************************************************
# [shaycraf@hills Ch07]$ python3 pe04.py
# Enter a series of 20 numbers:
# Enter the 1st number: 1
# Enter the 2nd number: 2
# Enter the 3rd number: 3
# Enter the 4th number: 4
# Enter the 5th number: 5
# Enter the 6th number: 6
# Enter the 7th number: 7
# Enter the 8th number: 8
# Enter the 9th number: 9
# Enter the 10th number: 10
# Enter the 11th number: 11
# Enter the 12th number: 12
# Enter the 13th number: 13
# Enter the 14th number: 14
# Enter the 15th number: 15
# Enter the 16th number: 16
# Enter the 17th number: 17
# Enter the 18th number: 18
# Enter the 19th number: 19
# Enter the 20th number: 20
# The total of the numbers you entered are:  210.0
# The average of the numbers you entered are:  10.5
# The lowest number you entered was:  1.0
# The highest number you entered was:  20.0
# [shaycraf@hills Ch07]$ cat pe04.py
# #Ch7 pe4
# #Description: This code asks user to enter a series of 20 numbers the returns the total of the
# #numbers entered, the average, the lowest and highest number entered.

# nums = []#list numbers are stored in the user enters
# order = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th',
# '13th','14th','15th','16th','17th','18th','19th','20th',]#list that showes the order of numbers entered
# total = 0#Accumulator
# print("Enter a series of 20 numbers:")

# for numbers in order:#loop that fills empty nums list by user entering numbers
#     nums.append(float(input('Enter the ' + numbers + ' number: ')))

# for num in range(len(nums)):#Loop that displays the total, min, max and aveerage of the numbers entered.
#     total += nums[num]
#     ave = total/len(nums)
#     mini = min(nums)
#     maxi = max(nums)

# print("The total of the numbers you entered are: ", total)
# print("The average of the numbers you entered are: ", ave)
# print("The lowest number you entered was: ", mini)
# print("The highest number you entered was: ", maxi)

# #Footer:

#     [shaycraf@hills Ch07]$

    