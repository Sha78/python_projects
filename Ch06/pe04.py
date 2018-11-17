#Ch06 pe04
#Description: ITEM COUNTER: 
#Assume a file containing a series of names (as Strings) is named names.txt and exists on the computer's disk. Write a rpogram that displays the number of names.
#that are stored in the file. (Hint: Open the file and read every string stored in it.  Use a variable to keep a count of the number of items that are read from the file.)


def mains():
  counter4 = 0
  try: 
    file_names = open('names.txt', 'r')
  except FileNotFoundError as err:
    print('File not found. exiting.')
  except DividedByZero as err:
    print('div/0!. exiting.')
  else:
    for name in file_names:
      counter4 += 1
    file_names.close()
    
  print('Total Names: ', counter4)  
  return
mains()

#THe footer sould be a copy and paste from the shell terminal. 
#***************************************************************************************************************************************************
#Ch06 pe02 
#Description:

#Write a program that asks the user for the name of the file. The program sould display only the first line of the file's content. 
#If the file contains less than five lines, it should display the files entire content. 

def main():
    counter2 = 0
  
    file_name = input('Enter file name: ')
    
    try: 
     file_object_name_file = open(file_name, 'r')
      
    except FileNotFoundError as err:
        print('No file of that name found')
    
    else: 
      for line in file_object_name_file:
        counter2 += 1
        
        
        if(counter <= 5):
          print(line)
        
        file_object_name_file.close()
      return
    main()
    
    #**************************************************************************************************************************************
    #Ch06 pe03
#Description: This code displays contents of a file with a number followed by a colon.  

#Write a program that asks the user for the name of a file. The program should display the contents of the file with each 
#line preceeded with a line number followed by a colon. 
#The line numbering should start at 1. 

file_name = input("Enter the name of the file: ")
counter =0
try:
  display_file = open(file_name, "r")
except FileNotFound as err:
  print('File not found. exiting.')
  
else:
  contents = display_file.readlines()

for line in contents:
  counter +=1
 
  print(counter,': ' + line)
display_file.close()
        
        
        
        
        
        
        
        
        
    
    