import turtle
import pygame


scr = turtle.Screen()
trt = turtle.Turtle()
scr.tracer(10,0)
scr.title("Graphics")
def goagain():
    scr.clear()
    trt.hideturtle()
    x = scr.numinput("Polygon Maker", 'How many sides?(3-10)',0,3,10)
    x = int(x)
    trt.goto(0,0)
    trt.pendown()
    trt.begin_fill()
    for j in range (0,x):
        trt.right(360/x)
        trt.forward(500/x)
    trt.penup()
    trt.goto(-300, -200)
    trt.write("{}-sided object".format(x), move=False, align="left", font=("Arial", 48, "normal"))
    trt.end_fill()
    return

scr.onscreenclick(goagain(),btn=1,add=True)
scr.listen()
scr.update()
scr.mainloop()