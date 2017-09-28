import turtle
wn = turtle.screen()
alex = turtle.Turtle()
colors = ["red","blue","green","orange"]
for color in colors:
    alex.color(color)
    for i in range(4):
        alex.forward(100)
        alex.penup()
        alex.forward(50)
        alex.pendown()
        alex.stamp()
        alex.left(90)
        print(i)
     alex.left(30)