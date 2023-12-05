import numpy as np 
from rgb import *

def Vector(x, y, z):
    return np.array([x,y,z])

def normsquared(vector):
    return np.sum(np.square(vector))

def norm(vector):
    return np.sqrt(normsquared(vector))

def dot(vector, otherVector):
    return vector.dot(otherVector)

def unitvector(vector):
    return vector / norm(vector)

# Utilities

def reflect(dir, normal):
    return dir - 2*dot(dir, normal) * normal

def random_unitVector():
    interval_teta = np.arange(0.0, 2 * np.pi, 0.001)
    interval_phi = np.arange(0.0, np.pi, 0.001)
    
    teta = np.random.choice(interval_teta)
    phi = np.random.choice(interval_phi)

    return Vector(np.cos(teta) * np.sin(phi), np.sin(teta) * np.sin(phi), np.cos(phi))

def random_inSphere():
    r = np.random.rand()

    return random_unitVector() * r

def gammacorrection(color):
    return RGB(*np.sqrt(color / 255))