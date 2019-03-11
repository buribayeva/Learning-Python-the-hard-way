animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def animal(index):
    if index == 1:
        an='first'
    elif index== 2:
        an='second'
    elif index == 3:
        an='third'
    else:
        an=str(index)+'th'

    print "The %s animal is at %d and is a %s" % (an, index-1, animals[index-1])
    print "The animal at %d is the %s animal and a %s" % (index-1, an, animals[index-1])

for i in range(1, 7):
    animal(i)
    
