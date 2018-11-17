def main():
  in_file = open('philosophers.txt', 'r')#opes file that is being read from, philosophers.txt.
  
  file_contents = in_file.read()#assigns a variable and read method to recently opened file.
  
  print(file_contents)#prints file contents
  
  in_file.close()#closes file so data is not lost. 
main()