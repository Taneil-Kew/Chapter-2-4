import turtle
wn=turtle.Screen()
pirate=turtle.Turtle

for i in steps:
    pirate.left(i)
    pirate.forward(100)
print(pirate.heading())