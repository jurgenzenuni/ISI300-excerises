#Exercise 8

import turtle
t=turtle.Pen()

#Setup
t.up()
t.goto(0, 0)
t.down()

for i in range(20):
    if i % 2 == 0:
        t.down()
        t.forward(150)
    else:
        for x in range(10):
            t.down()
            t.forward(10)
            t.up()
            t.forward(5)
    t.up()
    t.goto(0, t.ycor() -10)


