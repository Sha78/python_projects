#Assignment:  03A -intro
#Description: P.E. 3 through 5
#These programs determine if a person is an infant, child, teenager ot adult. 
#Displays Roman nuerals and converts an objects mass in weight.

age = int(input("Please enter your age: " )) 

if age<=1:
    print("You are: ", age , " You are an infant")
elif age==1 or age < 13:
    print("You are a child")
elif age == 13 or age<20:
    print("You are a teenager")
else:
    print("You are an adult")
    
    
    #----------------------------------------------------------------------------------------------------------
# [shaycraf@hills Ch03]$ python3 Pe03.py
# Please enter your age: 20
# You are an adult
# [shaycraf@hills Ch03]$ cat Pe03.py
# #Assignment:  03A -intro#Description: P.E. 3 through 5
# #These programs determine if a person is an infant, child, teenager ot adult.
# #Displays Roman nuerals and converts an objects mass in weight.

# age = int(input("Please enter your age: " ))

# if age<=1:
#     print("You are: ", age , " You are an infant")
# elif age==1 or age < 13:
#     print("You are a child")
# elif age == 13 or age<20:
#     print("You are a teenager")
# else:
#     print("You are an adult")


#     #----------------------------------------------------------------------------------------------------------



#     #-----------------------------------------------------------------------------------------------------------------

# [shaycraf@hills Ch03]$
