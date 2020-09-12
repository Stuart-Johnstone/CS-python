#INFORMATION FOR YOUR TA

from math import *
from decimal import Decimal
import turtle

# CONSTANTS
WIDTH = 800
HEIGHT = 600
AXISCOLOR = "black"

#creates the global vars for tracking global min/max
globMinCor = False
globMaxCor = False


#
#  Returns the screen (pixel based) coordinates of some (x, y) graph location base on configuration
#
#  Parameters:
#   xo, yo : the pixel location of the origin of the  graph
#   ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#   x, y: the graph location to change into a screen (pixel-based) location
#
#  Usage -> screenCoor(xo, yo, ratio, 1, 0)
#
#  Returns: (screenX, screenY) which is the graph location (x,y) as a pixel location in the window
#
def screenCoor(xo, yo, ratio, x, y):
    return (x*ratio) + xo,(yo + (y*ratio))

#
#  Returns a string of the colour to use for the current expression being drawn
#  This colour is chosen based on which how many expression have previously been drawn
#  The counter starts at 0, the first or 0th expression, should be red, the second green, the third blue
#  then loops back to red, then green, then blue, again
#
#  Usage -> getColor(counter)
#
#  Parameters:
#  counter: an integer where the value is a count (starting at 0) of the expressions drawn
#
#  Returns: 0 -> "red", 1 -> "green", 2 -> "blue", 3 -> "red", 4 -> "green", etc.
#
def getColor(counter):
    if counter == 0:
        return "red"
    elif counter == 1:
        return "green"
    elif counter == 2:
        return "blue"

#
#  Draw in the window an xaxis label (text) for a point at (screenX, screenY)
#  the actual drawing points will be offset from this location as necessary
#  Ex. for (x,y) = (1,0) or x-axis tick/label spot 1, draw a tick mark and the label 1
#
#  Usage -> drawXAxisLabelTick(pointer, 1, 0, "1")
#
#  Parameters:
#  pointer: the turtle drawing object
#  screenX, screenY): the pixel screen location to drawn the label and tick mark for
#  text: the text of the label to draw
#
#  Returns: Nothing
#
def drawXAxisLabelTick(pointer, screenX, screenY, text):# moves the pointer to the location of the tick and writes the tick
    pointer.penup()
    pointer.goto(screenX,screenY-10)
    pointer.pendown()
    pointer.goto(screenX,screenY+10)
    pointer.penup()
    pointer.goto(screenX,screenY+15)
    pointer.pendown()
    pointer.write(text)
    pass

#
#  Draw in the window an yaxis label (text) for a point at (screenX, screenY)
#  the actual drawing points will be offset from this location as necessary
#  Ex. for (x,y) = (0,1) or y-axis tick/label spot 1, draw a tick mark and the label 1
#
#  Usage -> drawXAxisLabelTick(pointer, 0, 1, "1")
#
#  Parameters:
#  pointer: the turtle drawing object
#  screenX, screenY): the pixel screen location to drawn the label and tick mark for
#  text: the text of the label to draw
#
#  Returns: Nothing
#
def drawYAxisLabelTick(pointer, screenX, screenY, text):
    pointer.penup()
    pointer.goto(screenX-10,screenY)
    pointer.pendown()
    pointer.goto(screenX+10,screenY)
    pointer.penup()
    pointer.goto(screenX+15,screenY)
    pointer.pendown()
    pointer.write(text)
    pass

#
#  Draw in the window an xaxis (secondary function is to return the minimum and maximum graph locations drawn at)
#
#  Usage -> drawXAxis(pointer, xo, yo, ratio)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#
#  Returns: (xmin, ymin) where xmin is minimum x location drawn at and xmax is maximum x location drawn at
#
def drawXAxis(pointer, xo, yo, ratio):
    pointer.penup()
    pointer.goto(0,yo)
    pointer.pendown()
    pointer.goto(800,yo)
    pointer.penup()
    pointer.goto(xo,yo)
    xmin = 0
    xmax = 800

    x = xo              #x pixel counter starting at xo
    num = 0             #general counter for tracking cart number
    while x < xmax:                                 #draws the positive x ticks 
        x += ratio                                  #increaces the x pixel counter by the pixel counter
        num += 1                                    #increaces the cart counter
        drawXAxisLabelTick(pointer,x,yo,str(num))

    x = xo
    num = 0
    while x > xmin:                                 #draws the negative x ticks
        x -= ratio
        num -= 1
        drawXAxisLabelTick(pointer,x,yo,str(num))
    return xmin, xmax

#
#  Draw in the window an yaxis 
#
#  Usage -> drawYAxis(pointer, xo, yo, ratio)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#
#  Returns: Nothing
#
def drawYAxis(pointer, xo, yo, ratio):
    #Draws the y asix
    pointer.penup()
    pointer.setpos(xo,0)
    pointer.pendown()
    pointer.setpos(xo,600)
    pointer.penup()
    pointer.goto(xo,yo)
    ymin = 0
    ymax = 600

    #draws the right ticks
    y = yo
    num = 0
    while y < ymax:
        y += ratio
        num += 1
        drawYAxisLabelTick(pointer,xo,y,str(num))

    #draws the left ticks
    y = yo
    num = 0
    while y > ymin:
        y -= ratio
        num -= 1
        drawYAxisLabelTick(pointer,xo,y,str(num))
    pass

#
#  Draw in the window the given expression (expr) between [xmin, xmax] graph locations
#
#  Usage -> drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#  expr: the expression to draw (assumed to be valid)
#  xmin, ymin : the range for which to draw the expression [xmin, xmax]
#
#  Returns: Nothing
#
def drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr):
    #Draw expression 
    exprMinCor = False
    exprMaxCor = False
    global globMaxCor                                           #Gets the global variables
    global globMinCor
    pointer.penup()
    x = xmin - (xo/ratio)                                       #gets the smallest cart X displayed

    for i in range(xmin,xmax):                                  #checks the value of y for every x pixel
        pointer.setpos(screenCoor(xo,yo,ratio,x,eval(expr))) #sets the pointer to the x and value and draws
        pointer.pendown()
        yprev = eval(expr)
        x+=(1/ratio)                                            #increaces the cart x by one pixel equivelent to ensure smooth lines 
        exprMinCor,exprMaxCor = checkMinMax(pointer,yprev,x,eval(expr),ratio,expr,exprMinCor,exprMaxCor)

    #Checks if the expr min/max is less or greater then the global min/max
    if exprMinCor != False and globMinCor != False:             #if both have val;ues
        if exprMinCor[1] < globMinCor[1]:                       #if the expr value is less then  he global value
            globMinCor = exprMinCor
    elif exprMinCor != False:                                   #if the global has no value
        globMinCor = exprMinCor                                 #expr value == global value

    if exprMaxCor != False and globMaxCor != False:
        if exprMaxCor[1] > globMaxCor[1]:
            globMaxCor = exprMaxCor
    elif exprMaxCor != False:
        globMaxCor = exprMaxCor

    #Prints the current expression min/max with the global min/max
    print("Expression Min: " + str(exprMinCor))
    print("Expression Max: " + str(exprMaxCor))
    print("Global Min: " + str(globMinCor))
    print("Global Max: " + str(globMaxCor))
    pass
    

#
#  checks if the current pointer cordinate is a min/ max
#  Usage -> checkMinMax(pointer, yPrev, x, y, ratio, expr, expMin, expMax)
#
#  Parameters:
#  pointer: the turtle drawing object
#  yPrev:  The previous y cordinate for the line
#  x, y :  the cartisean cordinate for the current pointer position
#  ratio:  the pixel to cart ratio
#  expr:   the original expression
#  expMin: the current minimum value for the expression
#  expMax: the current maximum value for the expression
#
#  Returns: expMin, expMax -> the new expression min/max


def checkMinMax(pointer,yPrev, x, y,ratio,expr,expMin,expMax):
    #gets the next y value
    x += 1/ratio
    yNew = eval(expr)

    #checks for a bend in the y values
    if yPrev >= y and y < yNew:
        #Draws the circle
        prevColor = pointer.color()
        pointer.color("orange")
        pointer.up()
        pointer.setheading(270)
        pointer.forward(5)
        pointer.setheading(0)
        pointer.forward(1)
        pointer.down()
        pointer.circle(5)
        pointer.up()
        pointer.color(prevColor[0])
        
        #checks if there is a expMin, if yes then it compares checks if the min is lower
        if expMin != False:
            if y < expMin[1]:
                expMin = [round(x-(1/ratio),8),round(y,8)]
        else:
            expMin = [round(x-(1/ratio),8),round(y,8)]

    elif yPrev <= y and y > yNew:
        prevColor = pointer.color()
        pointer.color("purple")
        pointer.up()
        pointer.setheading(270)
        pointer.forward(5)
        pointer.setheading(0)
        pointer.forward(1)
        pointer.down()
        pointer.circle(5)
        pointer.up()
        pointer.color(prevColor[0])

        #checks if there is a expMax, if yes then it compares checks if the max is heigher
        if expMax != False:
            if y > expMax[1]:
                expMax = [round(x-(1/ratio),8),round(y,8)]
        else:
            expMax = [round(x-(1/ratio),8),round(y,8)]
    return expMin,expMax


#
#  Setup of turtle screen before we draw
#  DO NOT CHANGE THIS FUNCTION
#
#  Returns: Nothing
#
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    pointer.speed(1000)     #increases the speed of the turtle
    return pointer

#
#  Main function that attempts to graph a number of expressions entered by the user
#  The user is also able to designate the origin of the chart to be drawn, as well as the ratio of pixels to steps (shared by both x and y axes)
#  The window size is always 800 width by 600 height in pixels
#  DO NOT CHANGE THIS FUNCTION
#
#  Returns: Nothing
#
def main():
    #Setup window
    pointer = setup()

    #Get input from user
    xo, yo = eval(input("Enter pixel coordinates of origin: "))
    ratio = int(input("Enter ratio of pixels per step: "))


    #Set color and draw axes (store discovered visible xmin/xmax to use in drawing expressions)
    pointer.color(AXISCOLOR)
    xmin, xmax = drawXAxis(pointer, xo, yo, ratio)
    drawYAxis(pointer, xo, yo, ratio)

    #Loop and draw experssions until empty string "" is entered, change expression colour based on how many expressions have been drawn
    expr = input("Enter an arithmetic expression: ")
    counter = 0
    while expr != "":
        pointer.color(getColor(counter))
        drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
        expr = input("Enter an arithmetic expression: ")
        counter += 1
        if counter == 3:
            counter = 0
 
#Run the program
main()
turtle.done()
