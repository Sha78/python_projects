def main():
  
  in_file = open('philosophers.txt', 'r')#assigns a var and opens file.
  
  line1 = in_file.readline()#assigns var and instructs program the first line to read. 
  line2 = in_file.readline()
  
  print(line1)#prints the first line in file. 
  print(line2)#prints second line in file.
  
  in_file.close()#closes file
  
main()#calls main function. 

#note: the thrid line in the file is not read bacause the program did not instruct it to be read. 