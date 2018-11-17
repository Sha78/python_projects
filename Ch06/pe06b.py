



import random
def main():
  file_output = open('random_numbers.txt', 'w')
  
  random_number_count = int(input('Number of values to create: '))
  for iter in range(random_number_count):
    file_output.write(str(random.randint(1,500)) + '\n')
   # print(random.randint(1,500)),
  file_output.close()
  return 

main()