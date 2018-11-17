#Ch4 Pe06 
#Description: This code converts Celcius to Farenheit. 

cel = 0 

print("Celcius" '\t''\t' "Farenheit")
print("-----------------------------")

for cel in range(0,21):
    far = (9/5*cel)+32
    print(cel, '\t''\t''\t', format(far, '.02f'))
    
    
#     ****************************************************
#     [shaycraf@hills Ch04]$ python3 pe06.pyCelcius         Farenheit
# -----------------------------
# 0                        32.00
# 1                        33.80
# 2                        35.60
# 3                        37.40
# 4                        39.20
# 5                        41.00
# 6                        42.80
# 7                        44.60
# 8                        46.40
# 9                        48.20
# 10                       50.00
# 11                       51.80
# 12                       53.60
# 13                       55.40
# 14                       57.20
# 15                       59.00
# 16                       60.80
# 17                       62.60
# 18                       64.40
# 19                       66.20
# 20                       68.00
# [shaycraf@hills Ch04]$