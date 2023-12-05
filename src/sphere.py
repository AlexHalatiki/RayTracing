from vector import *
import numpy as np
from hitRecord import *

class Sphere:
    def __init__(self, center, ray, material):
        self.center = center
        self.radius = ray
        self.material = material

    def hit(self, ray, t_min, t_max, record):
        # bhaskara
        oc = ray.origin - self.center
        a = normsquared(ray.direction)
        halfb = dot(ray.direction, oc)
        c = normsquared(oc) - self.radius**2
        discriminant = halfb**2 - a*c

        if discriminant < 0:
            return False

        t = (-halfb - np.sqrt(discriminant)) / a
        if t < t_min or t > t_max:
            t = (-halfb + np.sqrt(discriminant)) / a
            if t < t_min or t > t_max:
                return False
        
        record.t = t
        record.p = ray.origin + t * ray.direction
        outward_normal = unitvector(record.p - self.center)
        record.frontface = dot(ray.direction, outward_normal) < 0
        record.normal = outward_normal if record.frontface else -outward_normal
        record.material = self.material

        return True
