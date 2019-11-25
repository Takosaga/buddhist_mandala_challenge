import turtle

#intialize graphics
screen = turtle.Screen()
screen.title("Buddhist Mandala")
tracy = turtle.Turtle()
screen.bgcolor("black")

#outer cirlce of the mandala
def outer_circle():
    tracy.pendown()
    tracy.color("white")
    tracy.circle(300)

#moving up without leaving marks
def move_up():
    tracy.penup()
    tracy.left(90)
    tracy.forward(30)
    tracy.right(90)

#calling all functions
tracy.penup()
tracy.setposition(0,-300)
outer_circle()
move_up()

turtle.done()