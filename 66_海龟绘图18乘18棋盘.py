import turtle as t

width=30
num=18
x1=[(-400,400),(-400+width*num,400)]
y1=[(-400,400),(-400,400-width*num)]

t.speed(10)

# for i in range(0,19):
#     t.penup()
#     t.goto(x1[0][0],x1[0][1]-30*i)
#     t.pendown()
#     t.goto(x1[1][0],x1[1][1]-30*i)
# for i in range(0,19):
#     t.penup()
#     t.goto(y1[0][0]-30*i,y1[0][1])
#     t.pendown()
#     t.goto(y1[1][0]-30*i,y1[1][1])
for i in range(19):
    t.pendown()
    t.goto(-400,30*i)
    t.penup()
    t.goto(0,30*i)
    t.pendown()
    t.goto(-400,30*i)
t.done()