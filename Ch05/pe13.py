#Ch5 pe13
#Description: This program uses a function that accepts an object's falling time in secones as argument
#and returns the distance in meters it has fallen each second. 

def main():
  
   print("The distance an object falls per second.") 
   print("----------------------------------------")
   for time in range(1, 10 +1):
     fall = falling_distance(time)
      
     print(time,':00 second(s)', '\t', format(fall, '.2f'),'meter(s)')
      
def falling_distance(time): 
  
  distance = (1/2)*9.8*time**2

  return distance
main()
#***********************************footer for Ch5 pe13*********************************************
# [shaycraf@hills Ch05]$ python3 pe13.py
# The distance an object falls per second.
# ----------------------------------------
# 1 :00 second(s)          4.90 meter(s)
# 2 :00 second(s)          19.60 meter(s)
# 3 :00 second(s)          44.10 meter(s)
# 4 :00 second(s)          78.40 meter(s)
# 5 :00 second(s)          122.50 meter(s)
# 6 :00 second(s)          176.40 meter(s)
# 7 :00 second(s)          240.10 meter(s)
# 8 :00 second(s)          313.60 meter(s)
# 9 :00 second(s)          396.90 meter(s)
# 10 :00 second(s)         490.00 meter(s)
# [shaycraf@hills Ch05]$ cat pe13.py
# #Ch5 pe13
# #Description: This program uses a function that accepts an object's falling time in secones as argument
# #and returns the distance in meters it has fallen each second.

# def main():

#    print("The distance an object falls per second.")
#    print("----------------------------------------")
#    for time in range(1, 10 +1):
#      fall = falling_distance(time)

#      print(time,':00 second(s)', '\t', format(fall, '.2f'),'meter(s)')

# def falling_distance(time):

#   distance = (1/2)*9.8*time**2

#   return distance
# main()
# [shaycraf@hills Ch05]$
