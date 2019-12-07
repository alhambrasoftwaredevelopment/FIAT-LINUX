import random

import time

print (dir(time))

import turtle

classlist = ['Ramon', 'Awma Duh', 'Jessica', 'Alexis', 'Maria', 'Luke', 'Joseph', 'Jhonatan', 'Haley',
             'Patrick', 'Ernest', 'David', 'Tony', 'Julia', 'Erick', 'Vianka', 'Mya', 'Simanth', 'Sergio',
             'Eileen', 'Alfonso', 'Linda', 'Adriana', 'Jackie', 'Charles', 'Lestat', 'Efrain', 'Ren']

random.shuffle(classlist)
print (classlist[-1])

scr = turtle.Screen()
trt = turtle.Turtle()
scr.tracer(10, 0)
trt.penup()
scr.bgcolor("black")
trt.pencolor("white")
trt.setx(-200)
trt.sety(200)
trt.write("Good Morning, Sergio", move=False, align="left", font=("Arial", 40, "bold"))
trt.setx(-200)
trt.sety(100)
trt.write("This morning's weather is...", move=False, align="left", font=("Arial", 40, "bold"))
scr.mainloop()
