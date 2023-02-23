from PIL import Image, ImageDraw
import numpy as np
import math


def cardioid(r, step):
    img = Image.new("RGB", (600, 550), color=(0, 0, 255))
    draw = ImageDraw.Draw(img)
    l = []
    for t in np.arange(0, 2 * np.pi, np.pi / step):
        x = (2 * r * math.sin(t)) + (r * math.sin(2 * t))
        y = (2 * r * math.cos(t)) + (r * math.cos(2 * t))
        l.append(tuple([x + 300, y + 200]))
    draw.polygon(tuple(l), fill=(255, 0, 0))
    img.save("cardio.png")
    img.show()


cardioid(100, 6)
