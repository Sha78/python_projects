

def main():
  anum = int(input("enter your account number: ")) #Ask user to enter thier acount number.

  in_file= open('prac_list.txt', 'r')#open .txt file 
  prac_list= in_file.readlines()#readlines of .txt file 
  in_file.close()#close file
  line = 0 #initialize line counter
  while line != len(prac_list): #make a conditional loop that says to do something while the length of prac_list is the length of line. 
    prac_list[line] = int(prac_list[line])#convert lines to intergers
    line+= 1 #adds 1 to line every iteration of the loop
  if anum in prac_list: #compares the users input to each line in prac_list. 
    print("The number is valid.")
  else:
    print("The number is invalid")
    
 
  
  
main()
#*********************************************
# anum = input("enter your account number: ")

# fo= open('prac_list.txt', 'r')
# my_file= fo.readlines()
# for lines in my_file:
#   alist = [my_file]
  
  
  
  
 
  
# if anum in my_file:
#     print("The number is valid.")
# else:
#     print("The number is invalid")

# fo.close()