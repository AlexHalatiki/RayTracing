import numpy as np
from tqdm import tqdm
from random import random
from PIL import Image
from sphere import *
from vector import *
from ray import *
from rgb import *
from scene import *

def backgroundcolor(dir):
    t = (dir[1] + 1) * 0.5
    return (1-t) * RGB(1,1,1) + t * RGB(0.5,0.7,1)


def raycolor(ray, scene, depth = 50):
    if(depth <= 0):
        return RGB(0,0,0)

    record = HitRecord()

    if scene.hits(ray, 0.0001, float('inf'), record):
        shouldscatter, attenuation, direction = record.material.scatter(ray, record.normal)

        if shouldscatter:
            newray = Ray(record.p, direction)
            return RGB(*(attenuation / 255 * raycolor(newray, scene, depth-1) / 255))
        else:
            return RGB(0,0,0)

    return backgroundcolor(ray.direction)


def render(samples = 100):
    image = np.zeros((height, width, 3), dtype=np.uint8)

    for j in tqdm(range(height), desc="\033[92mRendering\033[0m"):
        for i in range(width):
            pixelcolor = RGB(0.0,0.0,0.0)
            for _ in range(samples):                
                u = (i + random()) / (width - 1)
                v = 1 - (j + random()) / (height - 1)
                dir = lowerleftcorner + u*horizontal + v*vertical - origin
                ray = Ray(origin, dir)
                pixelcolor += raycolor(ray, world)

            image[j][i] = gammacorrection(pixelcolor / samples)

    return Image.fromarray(image)


# IMAGE
aspectratio = 16/9
width = 800
height = int(width / aspectratio)

# CAMERA
viewportheight = 2
viewportwidth = viewportheight * aspectratio
horizontal = Vector(viewportwidth, 0, 0)
vertical = Vector(0, viewportheight, 0)
focallenght = 1
origin = Vector(0,0,0)
lowerleftcorner = origin - horizontal/2 - vertical/2 - Vector(0,0,focallenght)

# SCENE
bigradius = 100

materialfloor = Lambertian(RGB(0.8,0.8,0))
materialcenter = Lambertian(RGB(0.7,0.3,0.3))
materialleft = Metal(RGB(0.8,0.8,0.8))
materialrigth = Metal(RGB(0.8,0.6,0.2))

objects = {
    Sphere(Vector(0, 0, -1), 0.5, materialcenter),
    Sphere(Vector(-1, 0, -1), 0.5, materialleft),
    Sphere(Vector(1, 0, -1), 0.5, materialrigth),
    #Sphere(Vector(1.5, 0.2, -1.0), 0.5),
    Sphere(Vector(0, -bigradius - 0.5, -1), bigradius, materialfloor)
}

world = Scene()

for obj in objects:
    world.push(obj)

image = render()

image.save("./rendered/imagem10.png")