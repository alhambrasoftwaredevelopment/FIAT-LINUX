import random
import turtle

scr = turtle.Screen()
trt = turtle.Turtle()
turtle02 = turtle.Turtle()

turtle.color("red", "blue")
turtle02.color("green", 'yellow')
turtle.shapesize(3)
turtle02.shapesize(5)


def sender(btn, add):
    ace = random.randrange(-40, 40)  # size of blue shape
    cece = random.randrange(3, 10)  # number of sides of blue shape
    turtle02.penup()  # lift pen up
    turtle02.home()  # go to the center of the screen (0,0)
    turtle02.pendown()  # put the pen back down
    bb = turtle.position()  # sets a variable equal to the x and y of mouseclick
    aa = turtle02.towards(bb)  # assigns variable = direction from location to moutseclick
    turtle02.seth(aa)  # points second turtle at mouse click
    turtle02.goto(bb)  # turtle goes to mouse click
    turtle02.stamp()  # turtle stamps it's shape
    turtle.begin_fill()  # turtle fills color
    turtle.circle(ace, 360, cece)  # turtle draws shape
    turtle.end_fill()  # turtle fills color
    turtle.update()  # screen shows all the picture changes


scr.onclick(turtle.goto)
scr.onclick(sender, 1, True)

scr.listen()
scr.mainloop()
