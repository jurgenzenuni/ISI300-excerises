#EXERCISE 10

import turtle

Length = 15
Height = 10

pen = turtle.Pen()
pen.left(90)

for side in range(10):
    pen.forward(Height)
    pen.right(90)
    pen.forward(Length)
    pen.left(90)

turtle.exitonclick()
