#ch07 pe9 
#Description: This program reads a file into a list and outputs the smallest and largest populations years from the list.
#and outputs the average annual change in populations. 
    
def main():
  us_population = 'USPopulation.txt'
  total_population(us_population)#Calls total_pop function
  
def total_population(population_file_name):#defines the total_pop function that has us_population passed into it as an argument 
  total = 0
  count = 0
  annual_change_sum = 0
  year =1950
  us_population_list = []
  year_list = []
  us_population_file = open(population_file_name, 'r')
  
  for line in us_population_file:
    us_population_list.append(int(line.strip('\n')))#Reads files to list
    total += int(line.strip('\n'))#adds each line in the list with += operator
    count += 1
    
  if line == line.strip('\n'):
     average = total/count
  
  for lines in us_population_list:
    year_list.append(year)
    year +=1
    total += int(line.strip('\n'))#adds each line in the list with += operator
  
  
  max_increase_rate = 0 #process
  min_increase_rate = 1000000000
  max_increase_year = 1950
  min_increase_year = 1950
  for index in range(len(us_population_list)-1):
    increase_rate = population_growth_rate(us_population_list[index+1], us_population_list[index])
    
    if increase_rate > max_increase_rate:
      max_increase_rate = increase_rate
      max_increase_year = year_list[index+1]
    if increase_rate < min_increase_rate:
      min_increase_rate = increase_rate
      min_increase_year = year_list[index+1]
      
  for index in range(len(us_population_list)-1):
    change = average_yearly_change(us_population_list[index+1],us_population_list[index])
    annual_change_sum += change
  average_annual_change = annual_change_sum/len(us_population_list)
      
      

      
      
 
  
  print('The average annual change in population is: ',format(average_annual_change, '.2f')) 
  print('The year with the smallest increase in poulation is ', min_increase_year)
  print('The year with the greatest increase in poulation is: ', max_increase_year)
  
def average_yearly_change(list_begin, list_end):
  return list_begin-list_end


  
       
def population_growth_rate(population_endining, population_beginning):
  return population_endining/population_beginning-1

  
        
main()

################################################################################################################################################################
########################################################Footer for Ch07 pe9 Population Data#####################################################################
################################################################################################################################################################
# [shaycraf@hills Ch07]$ python3 pe7bAdv.py
# The average annual change in population is:  2384.27
# The year with the smallest increase in poulation is  1984
# The year with the greatest increase in poulation is:  1955
# [shaycraf@hills Ch07]$ cat pe7bAdv.py
# #ch07 pe9
# #Description: This program reads a file into a list and outputs the smallest and largest populations years from the list.
# #and outputs the average annual change in populations.

# def main():
#   us_population = 'USPopulation.txt'
#   total_population(us_population)#Calls total_pop function

# def total_population(population_file_name):#defines the total_pop function that has us_population passed into it as an argument
#   total = 0
#   count = 0
#   annual_change_sum = 0
#   year =1950
#   us_population_list = []
#   year_list = []
#   us_population_file = open(population_file_name, 'r')

#   for line in us_population_file:
#     us_population_list.append(int(line.strip('\n')))#Reads files to list
#     total += int(line.strip('\n'))#adds each line in the list with += operator
#     count += 1

#   if line == line.strip('\n'):
#      average = total/count

#   for lines in us_population_list:
#     year_list.append(year)
#     year +=1
#     total += int(line.strip('\n'))#adds each line in the list with += operator


#   max_increase_rate = 0 #process
#   min_increase_rate = 1000000000
#   max_increase_year = 1950
#   min_increase_year = 1950
#   for index in range(len(us_population_list)-1):
#     increase_rate = population_growth_rate(us_population_list[index+1], us_population_list[index])

#     if increase_rate > max_increase_rate:
#       max_increase_rate = increase_rate
#       max_increase_year = year_list[index+1]
#     if increase_rate < min_increase_rate:
#       min_increase_rate = increase_rate
#       min_increase_year = year_list[index+1]

#   for index in range(len(us_population_list)-1):
#     change = average_yearly_change(us_population_list[index+1],us_population_list[index])
#     annual_change_sum += change
#   average_annual_change = annual_change_sum/len(us_population_list)







#   print('The average annual change in population is: ',format(average_annual_change, '.2f'))
#   print('The year with the smallest increase in poulation is ', min_increase_year)
#   print('The year with the greatest increase in poulation is: ', max_increase_year)

# def average_yearly_change(list_begin, list_end):
#   return list_begin-list_end




# def population_growth_rate(population_endining, population_beginning):
#   return population_endining/population_beginning-1



# main()






# [shaycraf@hills Ch07]$
























      
   
      
      
     
      
      
      
      
      
      
    
     
     
        

        
        
        
