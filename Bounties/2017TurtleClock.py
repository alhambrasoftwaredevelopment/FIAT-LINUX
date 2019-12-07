import turtle

import time

print(dir(time))
scr = turtle.Screen()
scr.tracer(10, 0)
trt = turtle.Turtle()
while True:
    trt.goto(-300, 100)
    x = time.asctime()
    time.sleep(.001)
    scr.clear()
    trt.write(x, move="False", align="Left", font=("Arial", 30, "normal"))
    scr.update()
