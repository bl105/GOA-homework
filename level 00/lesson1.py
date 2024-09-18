from turtle import *


#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("pink")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)  #height of the door 
end_fill()
penup()
goto(200, 200)
pendown()
#end of a door

#drawing a roof

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of a roof

#drawing a window 
penup
goto(0, 0)
pendown
right(150)
forward(100)
right(100)
color("blue")
begin_fill()
forward(40)
left(100)
forward(40)
left(100)
forward(40)
left(100)
left(90)
right(110)
forward(26)
end_fill()
forward(5)


#end of one window

#drawing a second window 

color("pink")
penup
goto(0, 0)
pendown
left(90)
forward(201)

left(90)
forward(100)
color("blue")
begin_fill()
left(100)
forward(40)
right(100)
forward(40)
right(90)
forward(40)
right(90)
forward(34)
end_fill()

#end of the second window 

#drawing a grass
color("pink")
forward(100)
right(90)
forward(200)
color("green")
begin_fill()
forward(690)
left(180)
forward(9000)

end_fill()
#finnished the grass















exitonclick()