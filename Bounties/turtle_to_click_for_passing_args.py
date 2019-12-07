import random
import turtle

scr = turtle.Screen()
trt = turtle.Turtle()
turtle02 = turtle.Turtle()
turtle03 = turtle.Turtle()
turtle.color("red", "blue")
trt.hideturtle()
turtle03.shapesize(5)
turtle.speed("slow")
scr.tracer(2, 1)


def diddle(a, b, c):
    turtle03.penup()
    turtle03.home()
    turtle03.pendown()
    bb = turtle.position()
    aa = turtle03.towards(bb)
    turtle03.seth(aa)
    turtle03.goto(bb)
    # turtle02.penup()
    # turtle02.home()
    # turtle02.pendown()
    # turtle02.goto(a, b)
    # turtle.penup()
    # turtle.home()
    # turtle.pendown()
    # turtle.goto(aa)
    # turtle.begin_fill()
    # turtle.pendown()
    turtle.circle(a * .1, 360, c)
    # turtle.end_fill()
    turtle.update()


def sender(btn, add):
    ace = random.randrange(-400, 400)
    bece = random.randrange(-400, 400)
    cece = random.randrange(3, 10)
    diddle(ace, bece, cece)


scr.onclick(turtle.goto)
scr.onclick(sender, 1, True)

scr.listen()
scr.mainloop()
