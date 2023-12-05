from vector import *
from rgb import *

class Metal:
    def __init__(self, albedo = RGB(0.5,0.5,0.0), fuzz = 0):
        self.albedo = albedo
        self.fuzz = fuzz

    def scatter(self, ray, normal):
        reflecteddir = reflect(ray.direction, normal) + self.fuzz * random_inSphere()
        shouldscatter = dot(reflecteddir, normal) > 0
        return shouldscatter, self.albedo, reflecteddir
    

class Lambertian:
    def __init__(self, albedo = RGB(0.5,0.5,0.0)):
        self.albedo = albedo

    def scatter(self, ray, normal):
        scatterdir = normal + random_unitVector()
        if np.allclose(scatterdir, 0, atol=1e-8):
            scatterdir = normal

        return True, self.albedo, scatterdir