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

def white_cricle_accents():
    tracy.penup()
    for i in range(15):
        tracy.left(90)
        tracy.forward(7.5)
        tracy.pendown()
        tracy.color("red")
        tracy.pensize(3)
        tracy.right(180)
        tracy.forward(7.5)
        tracy.left(90)
        tracy.circle(245,12,20)
        tracy.left(90)
        tracy.forward(7.5)
        tracy.backward(7.5)
        tracy.right(90)
        tracy.penup()
        tracy.circle(245,12,20)




#calling all functions
tracy.penup()
tracy.speed(0)
tracy.setposition(0,-270)
outer_circle()
move_up(10)
rainbow_first_circle()
move_up(15)
tracy.begin_fill()
white_circle()
tracy.color("green")
tracy.end_fill()
white_cricle_accents()

turtle.done()