from sys import argv

script, filename=argv

print "We're going to erase %r." %filename
print "iF you don't want that,hit CTRL-C (^C)."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
target=open(filename,'r+')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1=raw_input("Line 1: ")
line2=raw_input("line 2: ")
line3=raw_input("line 3: ")

print "I'm going to write these file."

target.write('{}\n{}\n{}\n'.format(line1,line2,line3))
target.close()
a=open(filename)
b=a.read()
print "here our text %r"%b
a.close()
print "And finally , we close it."

