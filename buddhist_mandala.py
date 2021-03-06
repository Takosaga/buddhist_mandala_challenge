import turtle
import math

#intialize graphics
screen = turtle.Screen()
screen.title("Buddhist Mandala")
tracy = turtle.Turtle()
tracy.shape("turtle")
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

#the code to go around in white circle
def circle_sectors():
    tracy.left(90)
    tracy.forward(7.5)
    tracy.pendown()
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

#code to change the color of accents
def white_cricle_accents():
    tracy.penup()
    for i in range(15):
        if i % 3 == 0:
            tracy.color("cyan")
            circle_sectors()
        elif i % 3 == 1:
            tracy.color("green")
            circle_sectors()
        else:
            tracy.color("red")
            circle_sectors()

#decorations for innercircle
def inner_circle_deco():
    tracy.begin_fill()
    tracy.pendown()
    tracy.color("red")
    tracy.left(45)
    for i in range(4):
        tracy.forward(math.pi*200*2/12)
        tracy.right(135)
        tracy.circle(50,270)
        tracy.right(135)
        tracy.forward(math.pi*200*2/12)
        tracy.left(90)
    tracy.color("orange")
    tracy.end_fill()
    tracy.right(45)
    tracy.penup()

#marking the circles on the square
def circle_square_marks():
    circle_angle = math.degrees(math.asin(50/200))*2
    square_angle = (90 - circle_angle)/2
    tracy.pensize(2)
    tracy.color("black")
    for i in range(4):
        tracy.penup()
        tracy.circle(200,square_angle)
        tracy.pendown()
        tracy.circle(200,circle_angle)
        tracy.penup()
        tracy.circle(200,square_angle)

#marking circles with red accent in middle
def circle_square_marks_second():
    circle_angle = math.degrees(math.asin(50/170))*2
    square_angle = (90 - circle_angle)/2
    tracy.pensize(2)
    tracy.color("black")
    for i in range(4):
        tracy.penup()
        tracy.circle(170,square_angle)
        tracy.pendown()
        tracy.circle(170,circle_angle/3)
        tracy.color("red")
        tracy.right(90)
        tracy.forward(15)
        tracy.left(90)
        tracy.circle(185,circle_angle/3)
        tracy.left(90)
        tracy.forward(15)
        tracy.right(90)
        tracy.color("black")
        tracy.circle(170,circle_angle/3)
        tracy.penup()
        tracy.circle(170,square_angle)

#setting up inner square deco
def inner_sqaure_deco():
    side = math.sqrt(150*150 + 150*150)
    tracy.penup()
    tracy.left(90)
    for i in range(4):
        tracy.forward(150)
        tracy.begin_fill()
        tracy.backward(150)
        tracy.pendown()
        tracy.color("black")
        tracy.right(45)
        tracy.forward(side/2 - 10)
        tracy.right(90)
        tracy.forward(18)
        tracy.right(90)
        tracy.forward(10)
        tracy.left(90)
        tracy.forward(15)
        tracy.left(90)
        tracy.forward(40)
        tracy.left(90)
        tracy.forward(15)
        tracy.left(90)
        tracy.forward(10)
        tracy.right(90)
        tracy.forward(18)
        tracy.right(90)
        tracy.forward(side/2 - 10)
        tracy.penup()
        tracy.left(135)
        tracy.forward(150)
        if i % 4 == 0:
            tracy.color("cyan")
        elif i % 4 == 1:
            tracy.color("green")
        elif i % 4 == 2:
            tracy.color("red")
        else:
            tracy.color("yellow")
        tracy.end_fill()
        tracy.backward(150)

#circle right inside of inner square deco
def inner_inner_circle():
    tracy.pendown()
    tracy.color("purple")
    tracy.pensize(5)
    tracy.circle(100)

#final portion of inner circle
def final_circle_deco():
    tracy.color("black")
    tracy.pendown()
    tracy.circle(40)
    tracy.right(90)
    for i in range(5):
        if i % 3 == 0:
            tracy.color("green")
        elif i % 3 == 1:
            tracy.color("red")
        else:
            tracy.color("blue")
        tracy.circle(29,252)
        tracy.right(180)

#center of the circle
def tracy_turtle():
    tracy.penup()
    tracy.color("white")
    tracy.backward(40)
    tracy.shapesize(2,2,2)

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
move_up(45)
inner_circle_deco()
circle_square_marks()
move_up(30)
circle_square_marks_second()
move_up(20)
inner_sqaure_deco()
tracy.right(90)
move_up(50)
inner_inner_circle()
move_up(60)
final_circle_deco()
tracy_turtle()

turtle.done()