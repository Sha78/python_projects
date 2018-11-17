

TEAM = 'WorlSeriesWinners.txt'

def main():
  teams = []
  total = 0
  tfile = open(TEAM, 'r')
  myteam = input('Enter a team: ')

  for line in tfile:
    teams.append(line.strip('\n'))
    if myteam == line.strip('\n'):
      total+=1
  print(myteam, "has won the World Series", total, "times")

      
 
    

#   total =0
  
#   team_file = open(TEAM, 'r')
#   #print(type(team_file))
#   myteam = input("Enter team: ")
  
#   for line in team_file:
#     line.strip('\n')
#     total+=1
    
#   if myteam == line.strip('\n'):
    
#      print(total)
main()