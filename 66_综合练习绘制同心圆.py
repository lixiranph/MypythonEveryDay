import turtle
my_colors = ['red', 'green', 'blue', 'yellow', 'magenta']
turtle.bgcolor('black')
turtle.width(4)
turtle.speed(0)
for i in range(10): #i=0 i=1 i=2 i=3 i=4
    turtle.penup()
    turtle.goto(0,-i*10) #0, -100, -200, -300, -400
    turtle.pendown()
    turtle.color(my_colors[i%len(my_colors)])
    turtle.circle(30+i*10)      #100,200,300,400,500
turtle.hideturtle()
turtle.done()