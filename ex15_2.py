from sys import argv
script, filename=argv
prompt="> "
nfile=open(filename)
print "please say Hi"
hi=raw_input(prompt)
print nfile.read()
cfile=nfile.close()
print "file was closed"
