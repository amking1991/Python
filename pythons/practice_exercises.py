#print( "Hello") -----> string

#x = 5 -------> variable

import turtle

smart = turtle.Turtle()
#######draws the square -------->loop###########
#for i in range(4):
#    smart.forward(100)
#   smart.right(90)
#turtle.done()

#####draws the square#####
#smart.forward(100)
#smart.right(90)
#smart.forward(100)
#smart.right(90)
#smart.forward(100)
#smart.right(90)
#smart.forward(100)
#smart.right(90)


smart1 = turtle.Turtle()
######creating a square ------->function########
def square():
    smart1.forward(100)
    smart1.right(90)
    smart1.forward(100)
    smart1.right(90)
    smart1.forward(100)
    smart1.right(90)
    smart1.forward(100)
    
square() #<---------- must always call your function
#####make another square with current function#####
smart1.forward(100)
square()

import datetime

now = datetime.date(2015, 7, 14)

print(datetime.date.today().year)
