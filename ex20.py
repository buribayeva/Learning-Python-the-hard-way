from sys import argv #importing argv (list  which contains command lines) from sys module

script, input_file = argv # setting input_file our argument

def print_all(f): # creating new funtion with f argument
    print f.read() #calling read () function to open/read our input_file and print it

def rewind(f): # creating another new function with f argument
    f.seek(0) #calling seek() function to set read position , offset=0 wich means starting with the beginning of the file

def print_a_line(line_count, f): # creating new function to count lines of the input_file
    print line_count, f.readline() # printing file with line_count by calling readline() function

current_file=open(input_file) # calling open function to open input_file 

print "first let's print the whole file:\n" #printing simple text

print_all(current_file) # calling print_all function

print "now let's rewind, kind of like a tape." #another simple text

rewind(current_file) # calling rewind function

print "let's print three lines:"

current_line=1 # creating new variable with value 1
print_a_line(current_line, current_file) #calling print_a_line function and printing the first line of the file

current_line+=1 # 1+1 the secong line
print_a_line(current_line, current_file) #printing the second line by calling print_a_line function

current_line+=1 #2+1 
print_a_line(current_line,current_file) #printing 3d line of the file
