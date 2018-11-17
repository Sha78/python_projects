#Ch03 pe06
#Description: This program determines if the month, day and year is magic. A date where the month times the day equals the year  
print('\t\tMagic Date')
print('____________________________________________')
month = int(input('Enter a month in two digit numerical format: '))
day = int(input('Enter a day in two digit numerical format: '))
year = int(input('Enter a year in two digit numerical format:'))
           
           
if month * day == year:
  print('This is a Magic date !')
  
else:
  print('This is not a Magic date !')
  
#******************************footer for pe06****************************************************************
# [shaycraf@hills Ch03]$ python3 pe06.py              
# Enter a month in two digit numerical format: 09     
# Enter a day in two digit numerical format: 02       
# Enter a year in two digit numerical format:18       
# This is a Magic date !                              
# [shaycraf@hills Ch03]$ python3 pe06.py              
# Enter a month in two digit numerical format: 03
# Enter a day in two digit numerical format: 03
# Enter a year in two digit numerical format:90
# This is not a Magic date !
# [shaycraf@hills Ch03]$

##############################################################################################################
#*************************************************************************************************************
##############################################################################################################

#Ch3 pe07 
#Description: Color mixer. 
# PURPLE = [blue, red] 
# ORANGE = [red, yellow]
# GREEN = [blue, yellow]
print('\t\tColor Mixer')
print('\nEnter two colors out of: red, blue and yellow.' +
     '\nLetters typed must be lower case, correctly spelled' +
     '\nand there must be no spaces.')
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

########################################################################################################################
#***********************************************************************************************************************
########################################################################################################################

#Ch03 pe08
#Description: This code creates a hoedog cookout calculator to determine how much food is needed for the number of guests and hotdogs per guest the user enters. 
DOGS_PER_PACK =10 
BUNS_PER_PACK = 8

guest_count = int(input( ' Enter the number of people: '))
hotdogs_per_guest = int(input( ' Enter the number of hotdogs: '))

hotdogs_eaten = guest_count*hotdogs_per_guest

hotdog_pack_count = hotdogs_eaten//DOGS_PER_PACK

if hotdog_pack_count * BUNS_PER_PACK < hotdogs_eaten:
  hotdog_pack_count += 1
  hotdogs_uneaten_count = hotdog_pack_count * DOGS_PER_PACK - hotdogs_eaten
  
  
bun_package_count = 0
buns_uneaten_count = 0 

print('hotdog bun count', bun_package_count)
print('hotdogs uneaten', hotdogs_uneaten_count)
print('hotdog package count', hotdog_pack_count)
#************************************footer for Ch03 pe08************************************************



#########################################################################################################
#///////////////////////////////////////////////////////////////////////////////////////////////////////#
#*****************************   ************************************   ********************************#
#/////////////////////////////   ////////////////////////////////////   ////////////////////////////////#
#########################################################################################################
########################################################################################### ############
################  ######################################################################  ###############
##################  ##################################################################  #################
####################  #############################################################  ####################
#######################  ########################################################  ######################
#########################  ###################################################  #########################
###########################  ##############################################  ############################
##############################  ########################################  ###############################
################################  ###################################  ##################################
###################################  ##############################  ####################################
#####################################  #########################  #######################################
########################################  ###############################################################
###########################################  ############################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################                      ##########################################
#########################################################################################################









