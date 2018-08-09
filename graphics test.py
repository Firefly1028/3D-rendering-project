import mat
import numpy as np
from graphics import *


#Projection matrix for 3D on 2D screen
projection = [
    [1, 0, 0],
    [0, 1, 0]
]

points = []

def canvas():
    """Creates the window and canvas to draw on. Must be called, but takes no inputs"""
    #Creates the window and sets the background
    win = GraphWin('Creating a box in 2D', 500, 500)
    win.setBackground(color_rgb(0, 0, 0))

    draw(points, win)

    #Waits for a key press and then closes the window
    win.getKey()
    win.close()

def setup():
    points.append([150, 350, 0])
    points.append([350, 350, 0])
    points.append([150, 150, 0])
    points.append([350, 150, 0])

def draw(points: list, graphwin: GraphWin):
    #Draw points
    p1 = Circle(Point(points[0][0], points[0][1]), 8)
    p1.setFill(color_rgb(255,255,255))
    p1.draw(graphwin)

    p2 = Circle(Point(points[1][0], points[1][1]), 8)
    p2.setFill(color_rgb(255,255,255))
    p2.draw(graphwin)

    p3 = Circle(Point(points[2][0], points[2][1]), 8)
    p3.setFill(color_rgb(255,255,255))
    p3.draw(graphwin)

    p4 = Circle(Point(points[3][0], points[3][1]), 8)
    p4.setFill(color_rgb(255,255,255))
    p4.draw(graphwin)


setup()
canvas()