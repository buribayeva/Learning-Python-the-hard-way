def cheese_and_crackers(cheese_count, boxes_of_crackers): #defining new function cheese_and_crackers with two arguments
    print "You have %d cheeses!" %cheese_count #printing on the display one of the function's argument
    print "You have %d boxes of crackers!" % boxes_of_crackers # printing the second argument of our function
    print "Man that's enough for a party!" # printing just a simple text
    print "Get a blanket.\n" #staring with new line printing another simple text


print "We can just give the function numbers directly:" #prinintg text
cheese_and_crackers(20, 30) #calling our function with 20,30 arguments


print "OR, we can use variables from our script:" #printing another text
amount_of_cheese=10 #new value 1
amount_of_crackers=50  # another value

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # using two new values as arguments for our function in calling function


print "We can even do math inside too:" #another simple text
cheese_and_crackers(10+2, 5+6)#doing some simple math with function's arguments


print "And we can combine the two, variables and math:" # just simple text
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000) #calling our function with new created values and doing some math


