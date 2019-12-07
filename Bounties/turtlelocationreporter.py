import random
import turtle

scr = turtle.Screen()
turtle03 = turtle.Turtle()
scr.tracer(10, 0)
simon_pattern = []
for numbers in range(1, 100):
    x = random.randrange(1, 5)
    simon_pattern.append(x)

print (simon_pattern)
listlocs = []

turtle03.shape('circle')
turtle03.penup()
scr.tracer(10, 1)


def boardmaker():
    turtleblue = turtle.Turtle()
    turtlered = turtle.Turtle()
    turtlegreen = turtle.Turtle()
    turtleyellow = turtle.Turtle()
    turtleblue.shape('square')
    turtlered.shape('square')
    turtlegreen.shape('square')
    turtleyellow.shape('square')
    turtleblue.color('blue')
    turtlered.color('red')
    turtlegreen.color('green')
    turtleyellow.color('yellow')
    turtleblue.shapesize(10)
    turtlered.shapesize(10)
    turtlegreen.shapesize(10)
    turtleyellow.shapesize(10)
    turtleblue.goto(110, 110)
    turtlered.goto(110, -110)
    turtlegreen.goto(-110, 110)
    turtleyellow.goto(-110, -110)


def travelto(btn, add):
    wherenow = turtle03.position()
    wherenowx = int(turtle03.xcor())
    wherenowy = int(turtle03.ycor())
    listlocs.append(wherenowx)
    listlocs.append(wherenowy)
    turtle03.write(wherenowx, move=False, align='left', font=('Arial', 18, 'normal'))
    turtle03.write(wherenowy, move=False, align='right', font=('Arial', 18, 'normal'))
    # print(listlocs)
    scr.update()
    if wherenowx <= 210 and wherenowx >= 0 and wherenowy <= 210 and wherenowy >= 0:
        print('blue button clicked')
    if wherenowx <= 210 and wherenowx >= 0 and wherenowy >= -210 and wherenowy <= 0:
        print('red button clicked')
    if wherenowx >= -210 and wherenowx <= 0 and wherenowy <= 210 and wherenowy >= 0:
        print('green button clicked')
    if wherenowx >= -210 and wherenowx <= 0 and wherenowy >= -210 and wherenowy <= 0:
        print('yellow button clicked')


scr.onclick(turtle03.goto)
scr.onclick(travelto, 1, True)
scr.listen()
boardmaker()
scr.mainloop()
