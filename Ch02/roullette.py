#Assignment:  03A -intro
#Description: This program shows the color of a roulette poket from 0 to 36
#if a number from 0 to 36 is not entered an error message is shown.


print("Find out the color Roullette pocket the number is.")
num = int(input("Enter a number from 0 to 36: ")) 

if num == 0:
    print( num, " is in the green pocket")
elif num == 1 or num == 3 or num == 5 or num == 7 or num == 9:
    print( num, " is in a red pocket")
elif num == 2 or num == 4 or num == 6 or num == 8 or num == 10:
    print( num, " is in a black pocket")
elif num == 12 or num == 14 or num == 16 or num == 18:
    print( num, " is in a red pocket")
elif num == 11 or num == 13 or num == 15 or num == 17:
    print( num, " is in a black pocket")
elif num == 19 or num == 21 or num == 23 or num == 25 or num ==27:
    print( num, " is in a red pocket")
elif num == 20 or num == 22 or num == 24 or num == 26 or num == 28:
    print( num, " is in a black pocket")
elif num == 30 or num == 32 or num == 34 or num == 36:
    print( num, " is in a red pocket")
elif num == 29 or num == 31 or num == 33 or num == 35 :
    print( num, " is in a black pocket")
else:
    print("You entered", num, "that is an invalid entry.")
    print("Enter a number from 0 to 36 next time.")
    print("Try again!")
    
    #"""
#     [shaycraf@hills Ch02]$ python3 roullette.py
# Find out the color Roullette pocket the number is.
# Enter a number from 0 to 36: 30
# 30  is in a red pocket
# [shaycraf@hills Ch02]$ cat roullette.py#Assignment:  03A -intro
# #Description: This program shows the color of a roulette poket from 0 to 36
# #if a number from 0 to 36 is not entered an error message is shown.


# print("Find out the color Roullette pocket the number is.")
# num = int(input("Enter a number from 0 to 36: "))

# if num == 0:
#     print( num, " is in the green pocket")
# elif num == 1 or num == 3 or num == 5 or num == 7 or num == 9:
#     print( num, " is in a red pocket")
# elif num == 2 or num == 4 or num == 6 or num == 8 or num == 10:
#     print( num, " is in a black pocket")
# elif num == 12 or num == 14 or num == 16 or num == 18:
#     print( num, " is in a red pocket")
# elif num == 11 or num == 13 or num == 15 or num == 17:
#     print( num, " is in a black pocket")
# elif num == 19 or num == 21 or num == 23 or num == 25 or num ==27:
#     print( num, " is in a red pocket")
# elif num == 20 or num == 22 or num == 24 or num == 26 or num == 28:
#     print( num, " is in a black pocket")
# elif num == 30 or num == 32 or num == 34 or num == 36:
#     print( num, " is in a red pocket")
# elif num == 29 or num == 31 or num == 33 or num == 35 :
#     print( num, " is in a black pocket")
# else:
#     print("You entered", num, "that is an invalid entry.")
#     print("Enter a number from 0 to 36 next time.")
#     print("Try again!")

#     #"""[shaycraf@hills Ch02]$