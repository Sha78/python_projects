#Ch5 pe07
#Description: This code determines seating cost based on seating catigories. There are three seating catigories at a stadium. 
#Class A seats cost $20 , Class B seats cost $15, Class C seats cost $10. Write a program that asks how many tickets for each class of seats were sold, 
#then displays the amount of income generated from each ticket sale. 

def classA():

    return int(input("Enter class A seats sold: " )) 
def classB():
    
    return int(input("Enter class B seats sold: " )) 
def classC():

    return int(input("Enter class C seats sold: " )) 
    
a=classA()
b=classB()
c=classC()

print("The total amount of money generated from all ticket sales is: $", a*20 + b*15 +c*10)

# ************************************************
# [shaycraf@hills Ch05]$ python3 pe07.py
# Enter class A seats sold: 100
# Enter class B seats sold: 26
# Enter class C seats sold: 10
# The total amount of money generated from all ticket sales is: $ 2490
# [shaycraf@hills Ch05]$ cat pe07.py
# #Ch5 pe07
# #Description: This code determines seating cost based on seating catigories. There are three seating catigories at a stadium.
# #Class A seats cost $20 , Class B seats cost $15, Class C seats cost $10. Write a program that asks how many tickets for each class ofseats were sold,
# #then displays the amount of income generated from each ticket sale.

# def classA():

#     return int(input("Enter class A seats sold: " ))
# def classB():

#     return int(input("Enter class B seats sold: " ))
# def classC():

#     return int(input("Enter class C seats sold: " ))

# a=classA()
# b=classB()
# c=classC()

# print("The total amount of money generated from all ticket sales is: $", a*20 + b*15 +c*10)


#     [shaycraf@hills Ch05]$

    
    