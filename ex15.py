from sys import argv #importing argv from sys module

script, filename=argv # parametres of argv

txt=open(filename) # open function to open our file, txt is our new variable

print "Here's your file %r:" %filename # printing the file name -> ex15_sample.text
print txt.read() # view /read our file with read function where txt is the path to our file

print "Type the filename again:"
file_again=raw_input("> ") # using raw_input function we enter again the file name

txt_again=open(file_again) # using open funtion to open repeating file name

print txt_again.read() # rereading our file
