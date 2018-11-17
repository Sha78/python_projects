#Ch02 pe13
#Description: This program takes user input of length of a row, end-post space and space between vines 
#and calculates the number of plant that will be used. 

def main():
  #INPUT
  row_length = float(input('Enter the length of the row for grapevines in feet: '))
  end_post_space = float(input('Enter the space used by end post assembly in feet: '))
  space_between_grapevines = float(input('Enter the space between vines in feet: '))
  
  
  #processing
  number_of_grapevine_plants = (row_length - end_post_space*2)/space_between_grapevines#calculates the number of grapevine plants that can be planted in specified space. 
  
 
  #OUTPUT
  print('The number of grapevine you can have in the row is: ', int(number_of_grapevine_plants ))#prints number of grapevine plants. 
  
main()
  