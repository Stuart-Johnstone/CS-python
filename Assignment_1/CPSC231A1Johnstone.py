#Stuart Johnstone, CPSC231 LEC 01, TUT 04
#30086585
#Sept 19, 2019

#This program draws a circle on an axis then draws lines, 
#If the lines intersect the circle it highlights the intersection point with a circle.
#The program will keep prompting for lines until the user enters a blank input.

#Imports the module and creates the screen
#setup code and math is taken from the assignment outline
import turtle,math
pointer = turtle.Turtle()
screen = turtle.getscreen()
screen.setup(800,600, 0, 0)
screen.setworldcoordinates(0,0,800,600)
pointer.hideturtle()
pointer.speed(1000)

#moves the turtle to the center and draws the vertical axis
pointer.penup()#stops drawing
pointer.forward(400)
pointer.pendown()#starts drawing
pointer.left(90)
pointer.forward(600)
pointer.backward(300)
#draws the left axis
pointer.left(90)
pointer.forward(400)   
pointer.backward(400)
#draws the right axis
pointer.right(180)
pointer.forward(400)
pointer.backward(400)

#getting x,y cords and radius for circle
circleX = int(input("circle x cordinate: "))
circleY = int(input("circle y cordinate: "))
r = float(input("radius of circle: "))

#draws the main circle
pointer.penup()
pointer.setpos(circleX,circleY-r)#moves the turtle to a new pos
pointer.color("red")#changes the turtle color to red
pointer.pendown()
pointer.circle(r)#draws the circle


#this fuction is used to check if the line has a end point in the circle
def radCheck(cirX,cirY,rad,linX,linY):
    a = linX - cirX
    b = linY - cirY
    c = math.sqrt((a**2)+(b**2))#pythagoran therom

    if c < rad:
        return False
    else:
        return True

def corCheck(cor,num):#checks if an input is blank
    inp = input(cor+" value "+num + ": ")
    if inp == "":#returns a false if the input is blank
        return False
    else:
        return int(inp)

#creates a loop that gets input/ draws the lines
while True:
    #getting the start and stop points for the line
    print("enter a blank to stop the program")
    lineX1 = corCheck("x","1")
    if lineX1 == False:
        break
    lineY1 = corCheck("y","1")
    lineX2 = corCheck("x","2")
    lineY2 = corCheck("y","2")
    if False in [lineX1,lineY1,lineX2,lineY2]:#breaks the loop if the function returns a false
        break
    #gets the a/b/c values
    a = ((lineX2-lineX1)**2) + ((lineY2-lineY1)**2)
    b = 2*(((lineX1-circleX)*(lineX2-lineX1)) + ((lineY1-circleY)*(lineY2-lineY1)))
    c = ((lineX1-circleX)**2) + ((lineY1-circleY)**2) - (r**2)
    root = (b**2)-(4*a*c)-1#gets the square root of b^2 -4ac
    print(root)

    #draws the line
    pointer.penup()
    pointer.setpos(lineX1,lineY1)
    pointer.color("blue")
    pointer.pendown()
    pointer.setpos(lineX2,lineY2)

    if root < 0:#for the case of no intersect
        pointer.penup()
        pointer.setpos(350,300)
        pointer.pendown()
        pointer.color("green")
        pointer.write("No Intersects",font=("Ariel",20,"normal"))#writes the text

    elif root == 0:#for the case of one intersect
        alpha = (-b)/(2*a)#gets the alpha value using the quadratic formula
        x = (1-alpha)*lineX1 + alpha*lineX2
        y = (1-alpha)*lineY1 + alpha*lineY2
        pointer.penup()
        pointer.setpos(x,y-5)
        pointer.pendown()
        pointer.color("green")
        pointer.circle(5)

    elif root > 0:
        #when the root is above 0 the line starts in the circle or fully intersects through it
        #this requires a few cases for sorting the ammount of intersects 
        if radCheck(circleX,circleY,r,lineX1,lineY1) == False and radCheck(circleX,circleY,r,lineX1,lineY2) == False:#checks if the line is in the circle but doesn't instersect
            #writes no intersects
            pointer.penup()
            pointer.setpos(350,300)
            pointer.pendown()
            pointer.color("green")
            pointer.write("No Intersects",font=("Ariel",20,"normal"))
        
        elif radCheck(circleX,circleY,r,lineX1,lineY1) == False:#checks if the line starts in the circle but has one intersect
            #this math gets the x and y of the first intersept using the quadratic formula
            alpha = ((-b)+math.sqrt(root))/(2*a)
            x = (1-alpha)*lineX1 + alpha*lineX2
            y = (1-alpha)*lineY1 + alpha*lineY2
            #draws the circle for the intersect
            pointer.penup()
            pointer.setpos(x,y-5)
            pointer.pendown()
            pointer.color("green")
            pointer.circle(5)

        else:#for the case of two intersects
            #this math gets the x and y of the first intersept using the quadratic formula
            alpha1 = ((-b)+math.sqrt(root))/(2*a)
            x1 = (1-alpha1)*lineX1 + alpha1*lineX2
            y1 = (1-alpha1)*lineY1 + alpha1*lineY2
            #draws the circle for the first intersect
            pointer.penup()
            pointer.setpos(x1,y1-5)
            pointer.pendown()
            pointer.color("green")
            pointer.circle(5)

            #this math gets the x and y of the second intersept
            alpha2 = ((-b)-math.sqrt(root))/(2*a)
            x2 = (1-alpha2)*lineX1 + alpha2*lineX2
            y2 = (1-alpha2)*lineY1 + alpha2*lineY2
            #draws the circle for the second intesect
            pointer.penup()
            pointer.setpos(x2,y2-5)
            pointer.pendown()
            pointer.color("green")
            pointer.circle(5)

#finishes the turtle
turtle.done()