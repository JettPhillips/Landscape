import turtle

turtle.speed(.1)
turtle.color("green")
def square():
    for i in range(4):
        turtle.forward(30)
        turtle.right(90)

for i in range(80):
    turtle.right(5)
    square()




turtle.exitonclick()