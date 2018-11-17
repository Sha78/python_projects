#ch03 pe11
#Description: This program asks user to enter the number of book they purchased in a month and shows 
#how many book club award points they have been awarded. 

def main():
  print('Determine how many book club award points you have from your monthly book purchases.')
  number_books = int(input('Enter the number of books you bought this month: '))
  
  if number_books <= 1:# or number_books == 1:
    print('You earned zero points!')
    
  elif number_books == 2 or number_books == 3:
    print('You earned 5 points.')
  elif number_books == 4 or number_books == 5:
    print('You earned 15 points.')
  elif number_books == 6 or number_books == 7:
    print('You earned 30 points.')
  elif number_books >= 8:
    print('You earned 60 points.')
  
main()