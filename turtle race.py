import random
import turtle


jeyms = turtle.Turtle()
jeyms.speed(0)
jeyms.width(5)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

def up():
    jeyms.setheading(90)
    jeyms.forward(100)
    jeyms.penup()


def down():
    jeyms.pendown()
    jeyms.setheading(270)
    jeyms.forward(100)

def left(): 
    jeyms.setheading(180)
    jeyms.forward(100)
    jeyms.penup()

def right():
    jeyms.pendown()
    jeyms.setheading(0)
    jeyms.forward(100)

def clickleft(x, y):
    jeyms.color(random.choice(colors))

def clickright(x, y):
    jeyms.stamp()

turtle.listen()

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(right, 'Right')
turtle.onkey(left, 'Left')

turtle.mainloop()
    
