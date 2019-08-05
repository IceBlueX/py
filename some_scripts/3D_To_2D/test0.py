import turtle
pts = []
while True:
    line = input('请输入一个点的x，y坐标（如3,4），在空行回车结束输入：')
    if '' == line:
        break
    pts.append((int(line.split(',')[0]), int(line.split(',')[1])))
print(pts)
for i in range(len(pts)):
    for j in range(i+1, len(pts)):
        turtle.up()
        turtle.goto(pts[i])
        turtle.down()
        turtle.goto(pts[j])

turtle.done()