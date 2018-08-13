import pyxel
import numpy as np

points = [
    [-0.5, -0.5, 0.5],
    [0.5, -0.5, 0.5],
    [-0.5, 0.5, 0.5],
    [0.5, 0.5, 0.5],
    [-0.5, -0.5, -0.5],
    [0.5, -0.5, -0.5],
    [-0.5, 0.5, -0.5],
    [0.5, 0.5, -0.5]
]

xscale = 100
yscale = 100



class Cube:
    """Draw the cube onto the 2D screen. 
    Enter a matrix of coordinates for points.
    Enter a projection matrix for projectMat"""
    def __init__(self, points, scaleX, scaleY):
        self.points = points
        self.angle = 0
        self.scaleX = scaleX
        self.scaleY = scaleY
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

        projected = []
        i = 0

        for p in self.points:
            self.rotated = np.matmul(self.rotationX, vecToMat(p))
            self.rotated = np.matmul(self.rotationY, self.rotated)
            self.rotated = np.matmul(self.rotationZ, self.rotated)
            dist = 1 / (1.25 - self.rotated[2])
            projection = [
                [dist, 0, 0],
                [0, dist, 0]
            ]
            self.projection2d = matToVec(np.matmul(projection, self.rotated))
            self.projection2d[0] = self.projection2d[0] * self.scaleX
            self.projection2d[1] = self.projection2d[1] * self.scaleY

            projected.append(self.projection2d)
            pyxel.circ(self.projection2d[0] + pyxel.width/2, self.projection2d[1] + pyxel.height/2, 3, 7)
            i += 1
        
        connect(0, 1, projected)
        connect(0, 2, projected)
        connect(0, 4, projected)
        connect(1, 3, projected)
        connect(1, 5, projected)
        connect(2, 3, projected)
        connect(2, 6, projected)
        connect(3, 7, projected)
        connect(4, 5, projected)
        connect(4, 6, projected)
        connect(5, 7, projected)
        connect(6, 7, projected)

        self.angle += 0.02 # radians

def connect(i, j, points):
    a = points[i]
    b = points[j]
    pyxel.line(a[0] + pyxel.width/2, a[1] + pyxel.height/2, b[0] + pyxel.width/2, b[1] + pyxel.height/2, 8)

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

cube = Cube(points, xscale, yscale)