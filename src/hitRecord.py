from vector import *
from materials import *
from rgb import *

class HitRecord:
    def __init__(self, p = Vector(0,0,0), t = 0, normal = Vector(0,0,0), frontface = False, material = Metal(RGB(0,0,0))):
        self.p = p
        self.t = t
        self.normal = normal
        self.frontface = frontface
        self.material = material