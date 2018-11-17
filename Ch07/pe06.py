#Ch7 pe06
#Description: This program has a function that accepts two arguments, a list and a number. 
#The function displays all the numbers are greater than the number 


def main():
  num = 5 
  alist =[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20]
  func(alist, num)
def func(alist, num):#Function that accepts two arguments. alist is a list, num is a number
    
       print(alist[num:])#This is a slice that truncates the num argument and everything before it.
  
main()

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

# #Footer:
# #>>>>>>>>>>>>>>>>>>>>>>My other version of this exercise<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# #def main():
# #   num = 5 #int(input('Enter a number from 2-9: '))#Allows user to enter a number that is in the list
# #   alist =[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20]
# #   func(alist, num)
# # def func(alist, num):#Function that accepts two arguments. alist is a list, num is a number
# #     num = num
# #     if num<2 or num>9:
# #         print('try again')
# #     else:
# #        print(alist[num:])

# # main()



# #>>>>>>>>>>>>>>>Professors Solution<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# # def larger_than_n(search_list, pivot_n):
# #   for list_value in search_list:
# #     if list_value < pivot_n:
# #       print (list_value)
# #   return
# # def main():
# #   print('test 0-10, 5:')
# #   larger_than_n(range(10),5)
# #   print('test 0-10, 7:')
# #   larger_than_n(range(10),7)
# #   print('test 0-60, 23:')
# #   larger_than_n(range(60),23)
# # main()



#   [shaycraf@hills Ch07]$
#>>>>>>>>>>>>>>>>>>>>>>My other version of this exercise<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#def main():
#   num = 5 #int(input('Enter a number from 2-9: '))#Allows user to enter a number that is in the list
#   alist =[1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20]
#   func(alist, num)
# def func(alist, num):#Function that accepts two arguments. alist is a list, num is a number
#     num = num
#     if num<2 or num>9:
#         print('try again')
#     else:
#        print(alist[num:])
  
# main()



#>>>>>>>>>>>>>>>Professors Solution<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# def larger_than_n(search_list, pivot_n):
#   for list_value in search_list:
#     if list_value < pivot_n:
#       print (list_value)
#   return
# def main():
#   print('test 0-10, 5:')
#   larger_than_n(range(10),5)
#   print('test 0-10, 7:')
#   larger_than_n(range(10),7)
#   print('test 0-60, 23:')
#   larger_than_n(range(60),23)
# main()
  
  
  
  