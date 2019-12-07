import random
import turtle

b = turtle.Screen()
b.setup(width=.75, height=.75, startx=None, starty=None)
b.bgcolor("white")
colorr = 1

turtle.setheading(0)
turtle.pd()
turtle.tracer(0, 0)


def rightClick(btn, add):
    turtle.pensize(10)
    global colorr
    colorr = random.randrange(0, 8)
    if colorr == 0:
        b.bgcolor("white")
    elif colorr == 2:
        b.bgcolor("red")
    elif colorr == 2:
        b.bgcolor("orange")
    elif colorr == 3:
        b.bgcolor("yellow")
    elif colorr == 4:
        b.bgcolor("green")
    elif colorr == 5:
        b.bgcolor("blue")
    elif colorr == 6:
        b.bgcolor("indigo")
    elif colorr == 7:
        b.bgcolor("violet")
    elif colorr == 7:
        b.bgcolor("black")


def leftClick(btn, add):
    b.tracer(9, 0)
    sizetracker = random.randrange(-200, 100)
    sizetracker02 = random.randrange(-40, 40)
    colorR = hex(random.randrange(0, 255))
    colorG = hex(random.randrange(0, 255))
    colorB = hex(random.randrange(0, 255))
    print(colorR + colorG + colorB)

    print(colorR, colorG, colorB)
    for starz in range(1, 2):
        turtle.pu()
        turtle.setx(random.randrange(-500, 500))
        turtle.sety(random.randrange(-300, 300))
        turtle.pd()
        turtle.pensize(1)
        for times in range(0, 5):
            turtle.forward(sizetracker)
            turtle.circle(sizetracker02, 144, 100)
            for times in range(0, 5):
                turtle.forward(sizetracker02)
                turtle.circle(sizetracker02, 144, 100)


b.onclick(leftClick, 1, True)
b.onclick(rightClick, 3, True)

b.mainloop()
