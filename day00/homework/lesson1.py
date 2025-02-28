from turtle import*

#we want to paint a hous

#step 1:draw a square


color("blue")

width(7)
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
color("red")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("yellow")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()










#painting awindow

penup()
goto(150, 150)
pendown()


color("purple")
begin_fill()
right(150)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


penup()
goto(150, 150)
pendown


forward(142)


color("purple")
begin_fill()
right(90)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()
exitonclick()