#Ch06 pe02 
#Description:

#Write a program that asks the user for the name of the file. The program sould display only the first line of the file's content. 
#If the file contains less than five lines, it should display the files entire content. 

def main():
    counter = 0
  
    file_name = input('Enter file name: ')
    
    try: 
     file_object_name_file = open(file_name, 'r')
      
    except FileNotFoundError as err:
        print('No file of that name found')
    
    else: 
      for line in file_object_name_file:
        counter += 1
        
        
        if(counter <= 5):
          print(line)
        
        file_object_name_file.close()
      return
main()
  
  #*************************************************************************************************************************
# def main():
    
#     counter = 0 
    
#     file_name = input("Enter a file: ")
    
#     try: 
#       iput_file = open(file_name, 'r')
#     except FileNotFoundError as err: 
#       print('No file of that name found')
      
#     else:
#       for line in input_file:
#         counter += 1
        
        
#         if counter<=5: 
#           print(line)
#         input_file.close()
#       return
#     main()
      
    