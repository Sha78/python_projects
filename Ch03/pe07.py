#Ch3 pe7 
#Description: Color mixer. 
# PURPLE = [blue, red] 
# ORANGE = [red, yellow]
# GREEN = [blue, yellow]
print('\t\tColor Mixer')
print('\nEnter two colors out of: red, blue and yellow.' +
     '\nLetters must be lower case, correctly spelled' +
     '\nand have no spaces.')
print('_______________________________________________')


first_color_picked = input('Enter first color: ')
second_color_picked = input('Enter second color: ')



if (first_color_picked == 'blue' and second_color_picked == 'red') or (first_color_picked == 'red' and second_color_picked == 'blue' ):
  print(first_color_picked, 'mixed with',second_color_picked, 'makes Purple')
  
elif (first_color_picked == 'red' and second_color_picked == 'yellow') or (first_color_picked == 'yellow' and second_color_picked == 'red'):
  print(first_color_picked, 'mixed with',second_color_picked, 'makes Orange')
  
elif (first_color_picked == 'blue' and second_color_picked == 'yellow') or (first_color_picked == 'yellow' and second_color_picked == 'blue'):
  print(first_color_picked, 'mixed with',second_color_picked, 'makes Green')
  
else:
  print("You made an inccorrect choice or spelled the color wrong. Try again!")
  

#*****************************************footer for ch03 pe07*****************************************************************************
# [shaycraf@hills Ch03]$ python3 pe07.py
#                 Color Mixer

# Enter two colors out of: red, blue and yellow.
# Letters must be lower case, correctly spelled
# and have no spaces.
# _______________________________________________
# Enter first color: red
# Enter second color: blue
# red mixed with blue makes Purple
# [shaycraf@hills Ch03]$ python3 pe07.py
#                 Color Mixer

# Enter two colors out of: red, blue and yellow.
# Letters must be lower case, correctly spelled
# and have no spaces.
# _______________________________________________
# Enter first color: red
# Enter second color: yellow
# red mixed with yellow makes Orange
# [shaycraf@hills Ch03]$ python3 pe07.py
#                 Color Mixer

# Enter two colors out of: red, blue and yellow.
# Letters must be lower case, correctly spelled
# and have no spaces.
# _______________________________________________
# Enter first color: blue
# Enter second color: yellow
# blue mixed with yellow makes Green
# [shaycraf@hills Ch03]$






