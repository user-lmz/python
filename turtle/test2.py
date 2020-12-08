import turtle

turtle.fillcolor("red")
while True:
    turtle.forward(300)
    turtle.pos()
    turtle.right(144)
    turtle.pos()
    if abs(turtle.pos()) < 1:
        break

turtle.fd(116)
for i in range(5):
    turtle.fd(72)
    turtle.right(72)
turtle.end_fill()
turtle.done()