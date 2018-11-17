#ch03 pe13
#Description: This program asks user to enter the weight of a package and displays the shipping charge. 

def main():
  
 

  TWO_OR_LESS_LBS = 1.50
  THREE_TO_SIX_LBS = 3.00
  SEVEN_TO_TEN_LBS = 4.00
  OVER_TEN_LBS = 4.75

    package_weight = float(input('Enter the weight of package: '))

if package_weight<=2:
  print('You owe ', TWO_OR_LESS_LBS)
elif package_weight>2 and package_weight <= 6:
  print('You owe ', THREE_TO_SIX_LBS)
elif package_weight>6 and package_weight <= 10:
  print('You owe ',SEVEN_TO_TEN_LBS)
elif package_weight>10:
  print('You owe ',OVER_TEN_LBS)

    
    
main()