
#Ch7 pe05
#Description: 
#This program reads the contents of the file into a list. Then asks the user enter a charge account number 
#The program decides if the nuber entered is valid by searching the list.
#If the number is in the list the program shows a message that the number is valid.
#If the numberis not in the list the program displays a message that the number is not valid. 

def main():
    try:
        anum = int(input("enter your account number: ")) #Ask user to enter thier acount number.

        in_file= open('charge_account.txt', 'r')#open .txt file and assign it to in_file 
        account_list= in_file.readlines()#readlines of .txt file and assign it to prac_list
        in_file.close()#close .txt file
        line = 0 #initialize line counter

        while line != len(account_list): #akes a conditional loop
          account_list[line] = int(account_list[line])#convert .txt file a list with intergers
          line+= 1#iterates through lines of .txt file  

        if anum in account_list:#Checks to see if user entered a valid number or not.
          print("The number is valid.")
        else:
          print("The number is invalid")
    except ValueError:
          print("Error: use numbers only.")
    
   
     
main()

#*********************************Footer*****************************************************
# [shaycraf@hills Ch07]$ python3 pe05.py
# enter your account number: 1446891
# The number is valid.
# [shaycraf@hills Ch07]$ python3 pe05.py
# enter your account number: 1234567
# The number is invalid
# [shaycraf@hills Ch07]$ cat pe05.py

# #Ch7 pe05
# #Description:
# #This program reads the contents of the file into a list. Then asks the user enter a charge account number
# #The program decides if the nuber entered is valid by searching the list.
# #If the number is in the list the program shows a message that the number is valid.
# #If the numberis not in the list the program displays a message that the number is not valid.

# def main():
#   anum = int(input("enter your account number: ")) #Ask user to enter thier acount number.

#   in_file= open('charge_account.txt', 'r')#open .txt file and assign it to in_file
#   account_list= in_file.readlines()#readlines of .txt file and assign it to prac_list
#   in_file.close()#close .txt file
#   line = 0 #initialize line counter

#   while line != len(account_list): #akes a conditional loop
#     account_list[line] = int(account_list[line])#convert .txt file a list with intergers
#     line+= 1#iterates through lines of .txt file

#   if anum in account_list:#Checks to see if user entered a valid number or not.
#     print("The number is valid.")
#   else:
#     print("The number is invalid")


# main()


# [shaycraf@hills Ch07]$

#******************************pe06************************************************
#Ch7 pe06
#Description: This program has a function that accepts two arguments, a list and a number. 
#The function displays all the numbers are greater than the number 


# def main():
#   num = 5 
#   alist =[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20]
#   func(alist, num)
# def func(alist, num):#Function that accepts two arguments. alist is a list, num is a number
    
#        print(alist[num:])#This is a slice that truncates the num argument and everything before it.
  
# main()

#Footer:**********************Footer****************Footer***********************

# [shaycraf@hills Ch07]$ python3 pe06.py
# [6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20]
# [shaycraf@hills Ch07]$ cat pe06.py
# #Ch7 pe06
# #Description: This program has a function that accepts two arguments, a list and a number.
# #The function displays all the numbers are greater than the number


# def main():
#   num = 5
#   alist =[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20]
#   func(alist, num)
# def func(alist, num):#Function that accepts two arguments. alist is a list, num is a number

#        print(alist[num:])

# main()













