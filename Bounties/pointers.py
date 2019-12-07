import random
import turtle

scr = turtle.Screen()
trt = turtle.Turtle()
trt.penup()
trt.showturtle()
turtle.speed("slowest")
turtle.tracer(1, 1)


def sender(btn, add):
    bb = trt.position()
    for x in range(1, 10):
        xxx = random.randrange(-400, 400)
        yyy = random.randrange(-400, 400)
        trt.penup()
        turtle.penup()
        trt.goto(xxx, yyy)
        turtz = turtle.Turtle()
        turtz.penup()
        turtz.goto(xxx, yyy)
        turtz.shapesize(4)
        aa = turtz.towards(bb)
        turtz.towards(bb)
        turtz.seth(aa)
        turtz.pendown()
        turtz.forward(100)
        turtz.penup()
        scr.update()


scr.onclick(trt.goto)
scr.onclick(sender, 1, True)

scr.listen()
scr.mainloop()
