#EXERCISE 5

import turtle
t = turtle.Pen()

#setup
t.up()
t.goto(0, 0)
t.down()
t.right(90)

# Draw the lines
for i in range(10):
    t.forward(50)
    t.up()
    t.goto(t.xcor() + 10, 0)
    t.down()


