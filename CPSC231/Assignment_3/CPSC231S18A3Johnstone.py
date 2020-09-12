import sys
import os
import turtle
from pathlib import Path

WIDTH = 601
HEIGHT = 601
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"

def screenCoor(x, y):
    return (x*300) + 300,(300 + (y*300))

def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    turtle.bgcolor(BACKGROUNDCOLOR)
    pointer.up()
    pointer.speed(10000000)
    return pointer

def drawXTick(pointer, x, y, text):
    pointer.penup()
    pointer.goto(x,y-10)
    pointer.pendown()
    pointer.goto(x,y+10)
    pointer.penup()
    pointer.goto(x,y+15)
    pointer.pendown()
    pointer.write(text)
    pass

def drawYTick(pointer, x, y, text):
    pointer.penup()
    pointer.goto(x-10,y)
    pointer.pendown()
    pointer.goto(x+10,y)
    pointer.penup()
    pointer.goto(x+15,y)
    pointer.pendown()
    pointer.write(text)
    pass


def drawAxis(pointer):
    #the following code draws the axis
    pointer.color("blue")
    pointer.penup()
    pointer.goto(0,300)
    pointer.pendown()
    pointer.goto(600,300)
    pointer.penup()
    pointer.goto(300,300)
    pointer.penup()
    pointer.setpos(300,0)
    pointer.pendown()
    pointer.setpos(300,600)
    pointer.penup()
    pointer.goto(300,300)

    crtLst = [-1,-0.75,-0.5,-0.25,0,0.25,0.5,0.75,1]

    x = 0               #x pixel counter starting at 0
    y = 0               #y pixel counter starting at 0
    xo = 300            #the center x value
    yo = 300            #the center y value
    num = 0             #general counter for tracking cart number
    while num != 9:
        drawXTick(pointer,x,yo,crtLst[num])
        drawYTick(pointer,xo,y,crtLst[num])
        x += 75
        y += 75
        num += 1 
    pass

def importFile():
    names = False                                           #keeps track wether -names was called
    loop = False                                            #keeps track if the file name needs to be looped or not
    if len(sys.argv) == 1:                                  #if no other arguements are given
        loop = True
    elif len(sys.argv) <= 3:                                #if there are two extra arguements, it will check for the -names arguement
        if sys.argv[1] == "-names" and len(sys.argv) == 2:                         #if the arguement is -names then it will loop for valid files  
            names = True
            loop = True
        elif len(sys.argv) == 2:                            #if there is an arguement that isn't -names
            arg = sys.argv[1]
        elif "-names" in sys.argv:                          
            if sys.argv[1] == "-names":
                arg = sys.argv[2]
            else:
                arg = sys.argv[1]
        else:                                               #error for no manes
            print("neither arguement was -names")
            sys.exit(1)
    else:
        print("too many arguements")
        sys.exit(1)

    if loop == True:
        inpt = input("input a file name (press enter to quit)")
        while inpt != "" and loop == True:                  #loops untill the user quits or gives a correct file
            try:
                dat = open(inpt, 'r')
                print("file opened")
                loop = False
            except:
                print("file doesn't exist")
                inpt = input("input a file name (press enter to quit)")
        if inpt == "":
            sys.exit(1)
    else:                                                   #attempts to open the five given by arguements
        try:
            dat = open(arg, 'r')
            print("file opened")
        except:
            print("file doesn't exist")
            sys.exit(1)
    return dat, names

def starInfo():
    dat, arg = importFile()
    line = dat.readline()                                   #this stores the line data
    dct = {}                                                #creates thee dictionary that will be used fot the constilation function
    stars = []                                              #stores the star information in a list to be easily accesed later
    while line != "":
        line = line.rstrip()
        line = line.split(",")
        if ";" in line[-1]:
            line[-1] = line[-1].split(";")
            for i in range(len(line[-1])):
                dct[line[-1][i]] = (line[0],line[1],line[2])
        else:
            dct[line[-1]] = (line[0],line[1],line[2])
        stars.append((line[0],line[1],line[2]))             #adds the star information to a list containing all of the star information
        line = dat.readline()
    return stars, dct ,arg

#pointer -> Turtle drawing object
#stars -> list of tuples, contains (x,y,magnitude)
#starsDct -> dictionary, all of the named stars with their (x,y,magnitude)
#names -> boolean, tells the program wether to write the names or stars or not
def drawStars(pointer,stars,starsDct,names):
    for i in range(len(stars)):                                         #uses turtle to draw the stars, the cordinates are taken from the list of tuples
        x = float(stars[i][0])
        y = float(stars[i][1])
        mag = float(stars[i][2])
        pointer.up()
        pointer.color("grey")
        pointer.goto(screenCoor(x,y))
        pointer.down()
        pointer.begin_fill()
        pointer.circle((10 / (mag + 2)) / 2)
        pointer.end_fill()
    for k,v in starsDct.items():                                        #redraws the named stars in white
        x = float(v[0])
        y = float(v[1])
        mag = float(v[2])
        pointer.up()
        pointer.color("white")
        pointer.goto(screenCoor(x,y))
        pointer.down()
        pointer.begin_fill()
        pointer.circle((10 / (mag + 2)) / 2)
        pointer.end_fill()
        if names == True:                                               #if names is true then  the names of the stars is written
            pointer.write(k,font=("Arial", 5, "normal"))
        print(k,"is at (",v[0],v[1], ") with ", (10/(float(v[2])+2))/4, "magnitude")
    pass

#pointer -> the turtle obj
#starsDct -> the dictionary of stars, used for the names and xy cords

def loopConst(pointer,starsDct):                                            #Gets the constalation file
    inpt = input("input a constellation file name (press enter to quit)")
    counter = 1
    while inpt != "":                                                       #loops untill the user quits or gives a correct file
        try:
            dat = open(inpt, 'r')                                               #opens the file and stores the data
            print("file opened")
            constLst = readConst(dat)                                           #reads the data
            counter = colorConst(pointer,counter)
            drawConst(pointer, constLst, starsDct)                              #Draws the Constalation
            inpt = input("input a constellation file name (press enter to quit)")
        except:
            print("file doesn't exist")
            inpt = input("input a constellation file name (press enter to quit)")
    if inpt == "":                                                              #quits the program if the input is blank
        sys.exit(1)


#dat -> the fild data
def readConst(dat):
    datLst = []
    nameLst = []
    nameLst.append(dat.readline())                              #line data is added to a list
    line = dat.readline()                                       #new lind data
    while line != '':                                           #if the line isn[t blank then it appends it to a list
        line = line.rstrip("\n")
        line = line.split(',')
        datLst.append(line)
        if line[0] not in nameLst:
            nameLst.append(line[0])
        if line[1] not in nameLst:
            nameLst.append(line[1])
        line = dat.readline()
    print(nameLst[0], "constellation contains", nameLst[1:])
    return datLst

def colorConst(pointer, counter):
    if counter == 1:
        counter += 1
        pointer.color("red")
    elif counter == 2:
        counter += 1
        pointer.color("green")
    elif counter == 3:
        counter = 1
        pointer.color("yellow")
    return counter


def drawConst(pointer,constLst,  starsDct):
    for i in constLst:
        pointer.up()
        pointer.goto(screenCoor(float(starsDct[i[0]][0]),float(starsDct[i[0]][1])))
        pointer.down()
        pointer.goto(screenCoor(float(starsDct[i[1]][0]),float(starsDct[i[1]][1])))


def main():
    stars, starsDct, names = starInfo()
    pointer = setup()
    drawAxis(pointer)
    drawStars(pointer, stars, starsDct, names)
    loopConst(pointer,starsDct)
    turtle.done()

main()
