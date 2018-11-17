#Ch06 pe03
#Description: This code displays contents of a file with a number followed by a colon.  

#Write a program that asks the user for the name of a file. The program should display the contents of the file with each 
#line preceeded with a line number followed by a colon. 
#The line numbering should start at 1. 

        
        
file_name = input("Enter the name of the file: ")
counter =0

display_file = open(file_name, "r")
contents = display_file.readlines()

for line in contents:
  counter +=1
 
  print(counter,'. '+ line)
display_file.close()
