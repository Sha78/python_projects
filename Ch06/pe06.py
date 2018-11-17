#Ch6 pe06
#Description: This program calculates the average in all the numbers stored in the file 
#named number.txt

 

def main():
  total = 0 
  count = 0
  in_file = open('number.txt', 'r') #opens number.txt file 
  for line in in_file: #for loop counts and adds up the numbers in file. 
    new_val = int(line)
    total += new_val    
    count+=1
 
  average = int(total/count)#this calculates average, outside of the loop. 
  print('There are: ',line,' lines that total ', total)
  #print('The total is: ',total)
  print('The average is: ',average)
  in_file.close()

main()

#[shaycraf@hills Ch06]$ cat  pe06.py
#Ch6 pe06
#Description: This program calculates the average in all the numbers stored in the file 
#named number.txt
# def main():
#   total = 0 
#   count = 0
#   in_file = open('number.txt', 'r') #opens number.txt file 
#   for line in in_file: #for loop counts and adds up the numbers in file. 
#     new_val = int(line)
#     total += new_val    
#     count+=1
 
#   average = int(total/count)#this calculates average, outside of the loop. 
#   print('There are: ',line,' lines that total ', total)
#   #print('The total is: ',total)
#   print('The average is: ',average)
#   in_file.close()

# main()

# [shaycraf@hills Ch06]$ 

