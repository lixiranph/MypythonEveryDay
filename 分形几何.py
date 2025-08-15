import turtle

def draw_triangle(points, color, pen):
    pen.fillcolor(color)
    pen.up()
    pen.goto(points[0][0], points[0][1])
    pen.down()
    pen.begin_fill()
    pen.goto(points[1][0], points[1][1])
    pen.goto(points[2][0], points[2][1])
    pen.goto(points[0][0], points[0][1])
    pen.end_fill()

def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, depth, pen):
    colors = ['white', 'black', 'blue', 'red', 'green', 'yellow', 'purple']
    draw_triangle(points, colors[depth % len(colors)], pen)
    if depth > 0:
        sierpinski(
            [points[0],
             get_mid(points[0], points[1]),
             get_mid(points[0], points[2])],
            depth - 1, pen)
        sierpinski(
            [points[1],
             get_mid(points[0], points[1]),
             get_mid(points[1], points[2])],
            depth - 1, pen)
        sierpinski(
            [points[2],
             get_mid(points[2], points[1]),
             get_mid(points[0], points[2])],
            depth - 1, pen)

if __name__ == '__main__':
    pen = turtle.Turtle()
    pen.speed(0)
    screen = turtle.Screen()
    screen.bgcolor('white')

    # 初始大三角形的三个顶点
    vertices = [(-200, -150), (0, 200), (200, -150)]
    depth = 5  # 递归深度，越大细节越丰富，但越慢

    sierpinski(vertices, depth, pen)

    pen.hideturtle()
    screen.mainloop()

