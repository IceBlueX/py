# !/usr/bin/python
# -*- coding=utf-8 -*-
"""

# 3D点转换为2D点
输入3D点 输出2D点对应的图形

# 正轴测投影

[cos(a)  -sin(a)cos(b) 0 0      [0.7071  -0.4082  0 0
    0         cos(b)   0 0   =      0    0.8165   0 0
-sin(a)  -cos(a)sin(b) 0 0   =  -0.7071  -0.4082  0 0
    0           0      0 1]         0      0      0 1]

# 斜平行投影

[   1           0         0 0      [   1       0     0 0
    0           1         0 0   =      0       1     0 0
cot(a)cos(b) cot(a)sin(b) 0 0   =   0.3536  0.3536   0 0
    0           0         0 1]         0      0      0 1]

对于 斜等测图有 a = 45° cot(a) = 1
对于 斜二测图有 a = arcot(2)  cot(a) = 1/2  取b = 45°

所以采用斜二测有
x1 = x + 0.3536*z
y1 = y + 0.3536*z
"""

import turtle
# import matplotlib
# import cv

LENGTH = 200       # 立方体边长


class Point2D(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Point3D(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z


def from_3d_to_2d(p_3d):
    """
    斜二测投影 核心转换公式
    :param p_3d:
    :return:
    """
    p_2d = Point2D()
    p_2d.x = p_3d.x + 0.3536 * p_3d.z
    p_2d.y = p_3d.y + 0.3536 * p_3d.z

    return p_2d


def distance(p1, p2):
    """
    判断两点间的距离是否等于立方体的边长
    :param p1:
    :param p2:
    :return:
    """
    length = (p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2
    if length == LENGTH * LENGTH:
        return True
    return False


def draw_cubic(points_3d):
    """
    判断两点间的距离为立方体的边长 转换3D点为2D点并连接
    :param points_3d:
    :return:
    """

    for point in points_3d:
        for point1 in points_3d:
            if distance(point, point1):
                turtle.up()
                turtle.goto((from_3d_to_2d(point).x, from_3d_to_2d(point).y))
                turtle.down()
                turtle.goto((from_3d_to_2d(point1).x, from_3d_to_2d(point1).y))

    turtle.done()


def main():
    p_3d = [
        Point3D(0, 0, 0),
        Point3D(LENGTH, 0, 0),
        Point3D(0, LENGTH, 0),
        Point3D(0, 0, LENGTH),
        Point3D(LENGTH, LENGTH, 0),
        Point3D(0, LENGTH, LENGTH),
        Point3D(LENGTH, 0, LENGTH),
        Point3D(LENGTH, LENGTH, LENGTH),
    ]

    draw_cubic(p_3d)


# 执行
if __name__ == '__main__':
    main()

