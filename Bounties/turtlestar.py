import random
import turtle

quan = turtle.Turtle()
gilardo = turtle.Screen()
quan.color("red", "purple")

for xx in range(1, 5):
    quan.penup()
    quan.hideturtle()
    mott = random.randrange(20, 100)
    quan.goto(random.randrange(-400, 400), random.randrange(-400, 400))
    quan.seth(random.randrange(0, 360))
    quan.pendown()
    quan.showturtle()
    quan.begin_fill()
    for jones in range(0, 5):
        quan.forward(mott)
        quan.penup()
        quan.forward(mott * .618)
        quan.pendown()
        quan.forward(mott)
        quan.right(144)
    quan.end_fill()

gilardo.mainloop()
