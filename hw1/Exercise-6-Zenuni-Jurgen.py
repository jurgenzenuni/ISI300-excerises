#EXERCISE 6

import turtle
t=turtle.Pen()

# Set up the turtle
t.up()
t.goto(0, 0)
t.down()
solid_line = 10
non_visible_line = 5

# Draw 10 dashed horizontal lines, each 150 units long, with 10 units of space in between
for i in range(10):
    t.pensize(2)
    t.penup()
    t.goto(0, t.ycor() - 10)
    for x in range(15):
        t.forward(solid_line)
        t.up()
        t.forward(non_visible_line)
        t.down()
