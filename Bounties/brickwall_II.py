import turtle

b = turtle.Screen()
a = turtle.Turtle()

b.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.speed("fastest")
b.tracer(5, 0)
turtle.setheading(0)
turtle.pu()
turtle.setx(-960)
turtle.sety(-480)
turtle.pd()


def whereInX():
    global meeyo
    meeyo = turtle.xcor()
    return (meeyo)


def whereInY():
    global yuyo
    yuyo = turtle.ycor()
    return (yuyo)


def drawBrick():
    troodat = 1
    rowa = 1

    while troodat == 1:
        if rowa == 1:
            turtlesx = turtle.xcor()
            turtlesy = turtle.ycor()
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(100)
            turtle.update()
            if turtlesx >= 960:
                turtle.update()
                turtle.setx(-1010)
                turtle.sety(turtle.ycor() + 50)
            if turtlesy >= 0:
                break

    '''    for halfBrick in range(0,1):

        turtle.update()
        whereInX()
        whereInY()'''


def masterbuilder():
    drawBrick()


masterbuilder()

turtle.update()
b.mainloop()

'''
        if meeyo >= 980:
            if ww % 2 != 0:
                turtle.setx(-960)
                turtle.sety(yuyo+50)
            else:
                turtle.setx(-890)
                turtle.sety(yuyo+50)'''
