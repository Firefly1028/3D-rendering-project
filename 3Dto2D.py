import pyxel
import numpy as np

points = [
    [-25, -25, 25],
    [25, -25, 25],
    [-25, 25, 25],
    [25, 25, 25],
    [-25, -25, -25],
    [25, -25, -25],
    [-25, 25, -25],
    [25, 25, -25]
]

projection = [
    [1, 0, 0],
    [0, 1, 0]
]


class Cube:
    """Draw the cube onto the 2D screen. 
    Enter a matrix of coordinates for points.
    Enter a projection matrix for projectMat"""
    def __init__(self, points, projectMat):
        self.points = points
        self.angle = 0
        self.projectMat = projectMat
        self.projection2d = []
        self.rotated = []

        # Starts the program
        pyxel.init(500, 500, caption='3D Projection Into 2D Space')
        pyxel.run(self.update, self.draw)

    def update(self):
        self.rotationX = [
            [1, 0, 0],
            [0, np.cos(self.angle), -np.sin(self.angle)],
            [0, np.sin(self.angle), np.cos(self.angle)]
        ]
        self.rotationY = [
            [np.cos(self.angle), 0, np.sin(self.angle)],
            [0, 1, 0],
            [-np.sin(self.angle), 0, np.cos(self.angle)]
        ]
        self.rotationZ = [
            [np.cos(self.angle), -np.sin(self.angle), 0],
            [np.sin(self.angle), np.cos(self.angle), 0],
            [0, 0, 1]
        ]
        

    def draw(self):
        pyxel.cls(0)
        
        for p in self.points:
            self.rotated = np.matmul(self.rotationX, vecToMat(p))
            self.rotated = np.matmul(self.rotationY, self.rotated)
            self.rotated = np.matmul(self.rotationZ, self.rotated)
            self.projection2d = matToVec(np.matmul(self.projectMat, self.rotated))
            pyxel.circ(self.projection2d[0] + pyxel.width/2, self.projection2d[1] + pyxel.height/2, 3, 7)

        self.angle += 0.02 # radians

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

cube = Cube(points, projection)