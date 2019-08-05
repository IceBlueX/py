import turtle
"""
使用python3的turtle库绘制testerbang标志
"""
turtle.color('#05CDFF')
turtle.pensize(20)
turtle.circle(100)
turtle.penup()
turtle.goto(-60, 150)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('#05CDFF')
for i in range(1, 5):
    if i % 2 == 1:

        n = 120

    elif i % 2 == 0:

        n = 30

turtle.forward(n)

turtle.right(90)

turtle.end_fill()
turtle.penup()
turtle.goto(-15, 130)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('#05CDFF')
for i in range(1, 5):
    if i % 2 == 1:

        n = 30

    elif i % 2 == 0:

        n = 100

turtle.forward(n)

turtle.right(90)

turtle.end_fill()
turtle.penup()
turtle.goto(-30, 125)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('#FFFFFF')
turtle.pensize(1)
turtle.circle(10)
turtle.end_fill()
turtle.penup()
turtle.goto(30, 125)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('#FFFFFF')
turtle.pensize(1)
turtle.circle(10)
turtle.end_fill()
t = turtle.Turtle()
t.penup()
t.goto(-50, -55)
t.pendown()
t.write("测试帮", font=("微软雅黑", 28, "normal")) #fonttype有normal, bold, italic, underline
t.penup()
t.goto(-90, -85)
t.pendown()
t.write("专注测试技术推广落地", font=("Arial", 14, "bold")) #fonttype可以自由组合，如"bold italic"
turtle.done()
