import turtle

#intialize graphics
screen = turtle.Screen()
screen.title("Buddhist Mandala")
tracy = turtle.Turtle()
screen.bgcolor("black")

#outer cirlce of the mandala
def outer_circle():
    tracy.pendown()
    tracy.pensize(5)
    tracy.color("white")
    tracy.circle(270)

#moving up without leaving marks
def move_up(movement):
    tracy.penup()
    tracy.left(90)
    tracy.forward(movement)
    tracy.right(90)

#making rainbow circle 
def rainbow_first_circle():
    color_change = 60
    tracy.pendown()
    tracy.pensize(15)
    for i in range(color_change):
        if i % 5 == 0:
            tracy.color("blue")
            tracy.circle(260,360/color_change,color_change)
        elif i % 5 == 1:
            tracy.color("cyan")
            tracy.circle(260,360/color_change,color_change)
        elif i % 5 == 2:
            tracy.color("green")
            tracy.circle(260,360/color_change,color_change)
        elif i % 5 == 3:
            tracy.color("red")
            tracy.circle(260,360/color_change,color_change)
        else:
            tracy.color("orange")
            tracy.circle(260,360/color_change,color_change)

#makes another white inner circle
def white_circle():
    tracy.pendown()
    tracy.pensize(15)
    tracy.color("white")
    tracy.circle(245)

#calling all functions
tracy.penup()
tracy.speed(0)
tracy.setposition(0,-270)
outer_circle()
move_up(10)
rainbow_first_circle()
move_up(15)
white_circle()

turtle.done()