import pyxel
import matrixconversions
import numpy as np

angle = 0

points = [
    [100,100,0],
    [150,100,0],
    [100,150,0],
    [150,150,0]
]

class Cube:
    """Draw the cube onto the 2D screen. Enter a matrix of coordinates for points."""
    def __init__(self, points: list):
        self.points = points

        #Starts the program
        pyxel.init(500,500,caption='Creating a 3D cube on a 2D screen')
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        for p in self.points:
            pyxel.circ(p[0], p[1], 3, 11) #Draws a circle onto the screen at the coordinates of each point

Cube(points)