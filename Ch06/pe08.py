#Ch06 pe08 
#Description: This exercise assumes you have completed Prgramming exercise 7, 
#andom Number File Writer. Writre another program that reads the random numbers 
#from the file, displays the numbers, then displays the following data:
#The total of the numbers and The number of random numbers read fromthe file. 

# def main(): 
#   file_input = open(random_numbers.txt','r')
#   total = 0 
#   counter= 0 
                    
#   try: 
                    
#     file_input = open('random-numbers.txt', 'r')
#     for line in file_input:
#       print(line.rstrip('\n'))
#       total += int(line)
#       counter += 1
#     print('total', total)
#     print('counter', counter)
#     file_input.close()
#   except FileNotFound as err: 
#     print('File not found')
#   return
# main()
                    
#************************************************************************
def main():
  total = 0
  count = 0
try:
  
  random_number_file = open('random_numbers.txt', 'r')
  for line in random_number_file:
     new_value = int(line.rstrip('/n'))
     print(new_value)
     count += 1
     total += new_valueprint('total:', total)
     print('count:', count)
except FileNotFoundError as err:
  print('File not found.')
  random_number_file.close()
#return
main()