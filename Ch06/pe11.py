#Ch 06 pe11
#Description: This program asks user to enter name and self description then creates an html file containing users input for a simple web page. 

def main():


  #Open file to create. 
  create_web_page_file = open('created_web_page_file.html','w' )

  #Get name and self info from user

  name = input('Enter your name: ')
  profile = input('Describe yourself in a sentence: ')
  
  web_page_generator(name, profile, create_web_page_file)
  
 
def web_page_generator(name, profile, create_web_page_file):

  #Write the inputs to file. 

  create_web_page_file.write('<html>' + '\n')
  create_web_page_file.write('<head>' + '\n')
  create_web_page_file.write('</head>' + '\n')
  create_web_page_file.write('<body>' + '\n')
  create_web_page_file.write('\t'+'<center>' + '\n')
  create_web_page_file.write('\t'+'\t''<h1>' + name + '</h1>' + '\n')        
  create_web_page_file.write('\t'+'</center>' + '\n')
  create_web_page_file.write('\t'+'<hr>'+ '\n')
  create_web_page_file.write('\t'+ profile + '\n')
  create_web_page_file.write('\t'+'</hr> ' + '\n')
  create_web_page_file.write('</body>' + '\n')
  create_web_page_file.write('</html>' + '\n')

  #close the file
  create_web_page_file.close()
  print("Personal Web Page has been generated.")
  
  
  return 
 
  
main()

#*********************************footer for 02/06C-Mastery | Ch06 pe11********************************************************************************
# [shaycraf@hills Ch06]$ python3 pe11.py
# Enter your name: Shaman H.
# Describe yourself in a sentence: I am a student at CCSF learning python.
# Personal Web Page has been generated.
# [shaycraf@hills Ch06]$ cat pe11.py
# #Ch 06 pe11
# #Description: This program asks user to enter name and self description then creates an html file containing users input for a simple web page.

# def main():


#   #Open file to create.
#   create_web_page_file = open('created_web_page_file.html','w' )

#   #Get name and self info from user

#   name = input('Enter your name: ')
#   profile = input('Describe yourself in a sentence: ')

#   web_page_generator(name, profile, create_web_page_file)


# def web_page_generator(name, profile, create_web_page_file):

#   #Write the inputs to file.

#   create_web_page_file.write('<html>' + '\n')
#   create_web_page_file.write('<head>' + '\n')
#   create_web_page_file.write('</head>' + '\n')
#   create_web_page_file.write('<body>' + '\n')
#   create_web_page_file.write('\t'+'<center>' + '\n')
#   create_web_page_file.write('\t'+'\t''<h1>' + name + '</h1>' + '\n')
#   create_web_page_file.write('\t'+'</center>' + '\n')
#   create_web_page_file.write('\t'+'<hr>'+ '\n')
#   create_web_page_file.write('\t'+ profile + '\n')
#   create_web_page_file.write('\t'+'</hr> ' + '\n')
#   create_web_page_file.write('</body>' + '\n')
#   create_web_page_file.write('</html>' + '\n')

#   #close the file
#   create_web_page_file.close()
#   print("Personal Web Page has been generated.")


#   return


# main()[shaycraf@hills Ch06]$ cat created_web_page_file.html
# <html>
# <head>
# </head>
# <body>
#         <center>
#                 <h1>Shaman H.</h1>
#         </center>
#         <hr>
#         I am a student at CCSF learning python.
#         </hr>
# </body>
# </html>
# [shaycraf@hills Ch06]$