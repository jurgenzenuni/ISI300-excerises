#EXERCISE 7

import turtle
t=turtle.Pen()

# Set up the turtle
t.up()
t.goto(0, 0)
t.down()
t.right(90)

# Draw 10 dashed vertical lines, each 150 units long, with 10 units of space in between

for i in range(10):
    for x in range(15):
        t.forward(10)
        t.up()
        t.forward(5)
        t.down()
    t.up()
    t.goto(t.xcor() +10, 0)
