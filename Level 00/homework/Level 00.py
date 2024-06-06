from turtle import *


#we want to paint a house


#step 1: draw a spuare
speed(1)
width(6)
color("Green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawibd a door


forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#make windows

color("blue")
left(30)
forward(70)
left(90)
forward(50)
teleport(y=200, x=55 )
right(90)
forward(70)
right(90)
forward(10)

teleport(y=200, x=150)
left(90)
forward(70)
left(90)
forward(50)
left(90)
forward(70)
teleport(y=70, x=90)
left(90)
forward(20)


exitonclick()