def main():
  outFile = open('philosophers.txt', 'w')#opes file that is being written to.
  
  outFile.write('John Loke\n')#Writes to the file. notice there is an escape sequence to make a line break.
  outFile.write('Edmund Burke\n')
  outFile.write('Polato\n')
  outFile.write('Socretes\n')
  
  outFile.close()#closes file so data is not lost. 
main()