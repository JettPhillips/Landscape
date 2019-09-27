import turtle

turtle.color("red")
turtle.speed(.001)

def star(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(216)
def spiral():
    for i in range(60):
        star(2*i)
        turtle.right(5)
spiral()


turtle.exitonclick()
