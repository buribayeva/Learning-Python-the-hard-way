

def while_f(n) :
    numbers = []


    i = 0
    while i < n:
        print "At the top i is %d" % i
        numbers.append(i)

        i+= 2
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    print "The numbers: "
    for num in numbers:
     print num
print "please enter n "
n=int(raw_input("> "))

while_f(n)



