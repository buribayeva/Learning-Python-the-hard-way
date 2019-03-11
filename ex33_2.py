print "please enter n "
n=input("> ")

def while_f(n) :
    numbers = []
    i = 0
    start=0
    stop=n
    inc=2

    for i in range(start, stop, inc):
        print "At the top i is %d" % i
        numbers.append(i)
        #i+= 2
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    print "The numbers: "
    for num in numbers:
     print num


while_f(n)



