import turtle
wn=turtle.Screen()
pirate=turtle.Turtle
steps=[8352,86,94,42,16,954,32,08,50,460]
for i in steps:
    pirate.left(i)
    pirate.forward(100)
print(pirate.heading())