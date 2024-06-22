#EXERCISE 4

import turtle
t = turtle.Pen()

#setup
t.up()
t.goto(0, 0)
t.down()

#Draw the lines
for i in range(10):
    t.forward(50)
    t.up()
    t.goto(0, t.ycor() - 10)
    t.down()
    








