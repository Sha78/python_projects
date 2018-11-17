#Ch5 pe12
#Description:This program determines the large nuber in a function. 

def main():
  
  value_one = int(input("Enter a number: "))
  value_two = int(input("Enter another number: "))
  
  if value_one>value_two:
    lager_value=value_one
    
  else:
    lager_value = value_two
    
  print(lager_value, "is the larger value.")
  
  return True
  
main()

