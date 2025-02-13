#TurtleGraphics.py
#Name:Harrison Drake
#Date:02/12/25
#Assignment:Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(polygon, sides):
    for s in range(sides):
        polygon.forward(50)
        polygon.right(360/sides)
            
def fillCorner(jason, corner):
    drawSquare(jason, 100)
    
    if corner == 1:
        jason.begin_fill()
        drawSquare(jason, 50)
        jason.end_fill()
    elif corner == 2:
        jason.forward(50)
        jason.begin_fill()
        drawSquare(jason, 50)
        jason.end_fill()
    elif corner == 3:
        jason.forward(50)
        jason.right(90)
        jason.forward(50)
        penup()
        jason.begin_fill()
        pendown()
        drawSquare(jason, 50)
        jason.end_fill()
    elif corner == 4:
        jason.forward(100)
        jason.right(90)
        jason.forward(50)
        jason.begin_fill()
        drawSquare(jason, 50)
        jason.end_fill()
def squaresInSquares(myTurtle, num):
    size = 150
    for i in range(num):
        myTurtle.penup()
        myTurtle.goto(-size / 2,size / 2)
        myTurtle.pendown()
        drawSquare(myTurtle, size)
        size -= 20
        myTurtle.penup()
        myTurtle.goto(-size / 2,size / 2)
        myTurtle.pendown()

        
def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 3) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
