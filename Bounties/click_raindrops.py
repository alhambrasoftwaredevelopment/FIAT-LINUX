import turtle

scr = turtle.Screen()
trt = turtle.Turtle()
trt2 = turtle.Turtle()
scr.tracer(3, 0)
trt.hideturtle()
trt2.hideturtle()
trt.shape('circle')
trt2.shape('circle')
trt.color('blue')
trt2.color('white')


xposition = 0
yposition = 0
scr.listen()


def leftclick(x, y):
    maker = 1
    trt.penup()
    trt2.penup()
    trt.goto(x, y)
    trt2.goto(x, y)
    trt.pendown()
    trt2.pendown()
    for i in range(1, 100):
        trt.shapesize(maker * .05)
        trt2.shapesize(maker * .04)
        trt.stamp()
        trt2.stamp()
        maker += 1
        scr.update()
        trt.clearstamp(trt)


scr.onclick(leftclick)

scr.mainloop()
