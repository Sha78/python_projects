#Ch06 pe05
#Description: This program reads all the numbers stored in the file numbers.txt and calculates their total. 


def main():
  total = 0 #accumulator
  numbers_on_file = open('numbers.txt', 'r')#opens file to read from it
  
  for numbers in numbers_on_file:#for loop for getting a running count of numbers_on_file. 
    add_nums = float(numbers)
    total += add_nums #accumulator gathering numbers and storing them from add_nums 
    
    
  print("The total of all the numbers stored in the file, numbers.txt is: ", total)
  numbers_on_file.close()#closes file to exit program
  
main()

# [shaycraf@hills Ch06]$ python3 pe05.py
# The total of all the numbers stored in the file, numbers.txt is:  210.0
# [shaycraf@hills Ch06]$ 


    