import turtle

scr = turtle.Screen()
scr.tracer(3)
little_t = turtle.Turtle()
def clicky(btnname):
    for ernest in range(1, 300, 5):
        little_t.circle(100, 360, 5)
        print(ernest)
        little_t.forward(100)
        little_t.right(91)


scr.onclick("clicky", btn=1)
scr.listen()
scr.mainloop()