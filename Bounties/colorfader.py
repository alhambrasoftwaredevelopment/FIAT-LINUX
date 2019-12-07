import random
import sys
import turtle

import time

screen01 = turtle.Screen()
turtle01 = turtle.Turtle()

screen01.colormode(255)

redInit = random.randrange(0, 255)
redCyc = random.randrange(-2, 2)
greenInit = random.randrange(0, 255)
greenCyc = random.randrange(-2, 2)
blueInit = random.randrange(0, 255)
blueCyc = random.randrange(-2, 2)

# screen01.bgcolor(redInit, greenInit, blueInit)
while True:
    screen01.bgcolor(redInit, greenInit, blueInit)
    redInit = redInit + redCyc
    greenInit = greenInit + greenCyc
    blueInit = blueInit + blueCyc
    time.sleep(.01)
    print(redInit, redCyc, greenInit, greenCyc, blueInit, blueCyc)
    if (redInit) <= 0:
        time.sleep(.01)
        redInit = 252
    elif (redInit) >= 252:
        time.sleep(.01)
        redInit = 0
    elif (greenInit) <= 0:
        time.sleep(.01)
        greenInit = 252
    elif (greenInit) >= 252:
        time.sleep(.01)
        greenInit = 0
    elif (blueInit) <= 0:
        time.sleep(.01)
        blueInit = 252
    elif (blueInit) >= 252:
        time.sleep(.01)
        blueInit = 0
    elif (blueInit) <= 0:
        time.sleep(.01)
        blueInit = 252
    else:
        print("yadoneitnow")


def timeToFly():
    sys.exit()


screen01.listen()
screen01.onkey(timeToFly, "Up")
# screen01.onkey(numberGetter, "Down")
screen01.exitonclick()
screen01.mainloop()
