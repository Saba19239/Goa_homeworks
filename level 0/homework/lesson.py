from turtle import *

#we want to paint a house
speed(30)
width(7)
shape("turtle")
color("orange")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("orange")
left(30)
forward(120)

penup()
goto(30,150)
pendown()

color("brown")

forward(30)
left(90)

forward(30)
left(90)

forward(30)
left(90)

forward(30)
left(90)



penup()
goto(150,150)
pendown()


forward(30)
left(90)

forward(30)
left(90)

forward(30)
left(90)

forward(30)
left(90)




forward(25)
exitonclick()

