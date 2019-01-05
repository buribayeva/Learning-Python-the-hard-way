x="There are %d types of people." %10 #here is interger 10 varuable 
binary= "binary" #just string
do_not= "don't" #another string
y="Those who know %s and those who %s." % (binary, do_not) #putting string inside the str

print x #printing out x
print y #printing out y

print "I said: %r." % x # putting str inside str
print "I also said: '%s'." % y # another str inside str

hilarious=False #boolean value
joke_evaluation = "Isn't that joke so funny?! %r" #str value

print joke_evaluation % hilarious #printing str+boolean

w="This is the left side of..." #str
e="a string with a right side." #str

print w+e #sum two different str
