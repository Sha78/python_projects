
# # This program reads and displays contents in a file. 
# def main(): 
#     #open file named names.txt
#     infile = open('names.txt', 'r')
    
#     #Read the files content
#     file_contents = infile.read()
    
#     #close the file
#     infile.close()
    
#     #Print data that was read into memory
    
#     print(file_contents)
    
#   #call the main function
# main()
  
  #****************************************************************************************************************
  #THis is just some code to work from
# file_name = input("Enter file name: " )
# counter = 0
# display_it = open(file_name, 'r')
# contents = display_it.read()
    
# for num in contents:
 
#     counter += 1
    
#     print(counter,': ', contents)
    
#     display_it.close()

#*********************************************************************************************************************

# def main():
#   file_name = input("Enter the name of the file: ")
#   display_contents = open(file_name)
#     for line in file_name:
#       counter += 1
#         print(counter,': ',display_contents)
#**************************************************************

# file_name = input("Enter the name of the file: ")
# counter =0
# display_file = open(file_name, "r")
# contents = display_file.readlines()

# for line in contents:
#   counter +=1
 
#   print(counter,': ' + line)
# display_file.close()

#************************************************************
file_name = input("Enter the name of the file: ")
counter =0
try:
  display_file = open(file_name, "r")
except FileNotFound as err:
  print('File not found. exisiting')
  contents = display_file.readlines()

for line in contents:
  counter +=1
 
  print(counter,': ' + line)
display_file.close()
        


  
        
  
  