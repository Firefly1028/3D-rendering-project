import numpy as np


#Converts a vector to a matrix
def vecToMatrix(v):
    """Takes a vector, v, and inserts it into a 3 row, single column matrix"""
    m = []
    m.append([v[0]])
    m.append([v[1]])
    m.append([v[2]])
    return m

#Converts a matrix to a vector
def matrixToVec(m):
    """Takes a matrix, m, and converts it to a vector"""
    v = []
    v.append(m[0])
    v.append(m[1])
    if(len(m) > 2):
        v.append(m[2])
    return v

#Makes program more compact by converting and multiplying the vector and matrix in one function
def matVecMul(matrix, vector):
    """Multiplies a matrix and a vector by converting the vector to a matrix.
    A matrix should be entered for param 1.
    A vector should be entered for param 2."""
    m = vecToMatrix(vector)
    return np.matmul(matrix, m)

def setup(v, projection):
    result = matVecMul(projection, v) #Multiplies the projection and the point (previousy v, but has now been converted to a matrix named 'point')
    v = matrixToVec(result) #Converts the result into a new vector and stores it 'v'