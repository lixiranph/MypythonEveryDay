import turtle#导入turtle模块
while True:
    turtle.showturtle() #显示箭头
    turtle.write('高淇')#写个字符串
    turtle.forward(300)#前进300像素
    turtle.color('red')#画笔颜色改为红色
    turtle.left(90)#箭头左转90度
    turtle.forward(300)#前进300像素
    turtle.goto(0,50)#去到坐标（0，50）
    turtle.goto(0,0)#去坐标（0，0）
    turtle.penup()#抬笔，这样路径不会画出来
    turtle.goto(0,300)#去坐标（0，300）
    turtle.pendown()#下笔
    turtle.circle(100)#画个全大小100个像素