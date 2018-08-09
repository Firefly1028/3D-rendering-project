import pyxel
import numpy as np

points = [
    [100, 100, 0],
    [150, 100, 0],
    [100, 150, 0],
    [150, 150, 0]
]

projection = [
    [1, 0, 0],
    [0, 1, 0]
]


class Cube:
    """Draw the cube onto the 2D screen. Enter a matrix of coordinates for points."""
    def __init__(self, points):
        self.points = points
        self.angle = 0
        self.projection2d = []
        self.rotated = []

        # Starts the program
        pyxel.init(500, 500, caption='Creating a 3D cube on a 2D screen')
        pyxel.run(self.update, self.draw)

    def update(self):
        self.angle += 0.01
        self.rotation = [
            [np.cos(self.angle), -np.sin(self.angle)],
            [np.sin(self.angle), np.cos(self.angle)]
        ]

    def draw(self):
        pyxel.cls(0)
        for p in self.points:
            self.projection2d = vecToMat(np.matmul(projection, p))
            self.rotated = matToVec(np.matmul(self.rotation, self.projection2d))
            print("Projection2D:", self.projection2d)
            print("Rotation:", self.rotation)
            print("Matmul:", np.matmul(self.rotation, self.projection2d))
            print("Rotated:", self.rotated)
            # Creates a point for each projected 3D point into 2D
            pyxel.circ(self.rotated[0], self.rotated[1], 3, 7)


def vecToMat(vector):
    m = []
    for i in vector:
        m.append([i])
    return m

def matToVec(matrix):
    v = [0] * len(matrix)
    for i in range(len(matrix)):
        v[i] = matrix[i][0]
    return v

Cube1 = Cube(points)