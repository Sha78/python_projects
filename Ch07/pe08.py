
#Ch07 pe08
#Description: Write a program that reads the contents of the two files into two separate 
#lists. 
#The user should be able to enter a boy’s name, a girl’s name, or both, and the 
# #application will display messages indicating whether the names were among the most popular.
def main():
  
  girln =[]
  #girln = input('Enter a girls name: ')
  girlf = open('girlnames.txt', 'r')
  girlr = girlf.readlines()
  
 
  for names in girlf:
     girln = input('Enter a girls name: ')
    
  if girln in girlf:

    print(girln, 'Is there')
    
    #if girl_name_entered in girl_names       
main()
    
    
    
# NE =3
# def main():
#   hours =[0] *NE
#   for index in range(NE):
#     print('Enter hours worked by Employee: ')
#     hours[index] = float(input())
#   pay = float(input('Enter pay: '))
  
#   for index in range(NE):
  
#     gross = hours[index] * pay
#     print(index + 1, gross) 
    
# main()
  
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   

    


  
   
    
 
  

  
  
  