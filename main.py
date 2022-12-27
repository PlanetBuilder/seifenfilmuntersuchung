import math
import time

from PIL import Image
import colour
import matplotlib.pyplot as plt
import numpy as np


def distance(num1, num2):
    return math.sqrt((num2 - num1) ** 2)


def rgb_int(rgb_value):
    return 65536 * rgb_value[0] + 256 * rgb_value[1] + rgb_value[2]


# read wavelengths file and store it in array
f = open("wavelengths.txt", "r")
wavelengthsString = f.read().replace("[", "").replace("]", "").split(", ")
rgb_wavelengths = []
for i in range(16777216):
    rgb_wavelengths.append(int(wavelengthsString[i]))

# read image
img = Image.open("DSC_0100.png", "r", None)
rgb_im = img.convert('RGB')
img_rgbs = []
for x in range(rgb_im.width):
    print("Indexing image: ", x, "/", rgb_im.width)
    img_rgbs.append([])
    for y in range(rgb_im.height):
        img_rgbs[x].append(rgb_im.getpixel((x, y)))

# set image width and height as constants
img_width = min(rgb_im.width, rgb_im.height)
img_height = img_width

print(1)
# get thickness values for each pixel
thickness_values = []
for x in range(int(img_width)):
    print(x)
    thickness_values.append([])
    for y in range(int(img_height)):
        # get rgb value of pixel
        rgb = img_rgbs[x][y]

        # get dominant wavelength of pixel
        dom_wl = rgb_wavelengths[rgb_int(rgb)]
        if dom_wl < 0:
            dom_wl = -dom_wl + 125
        thickness_values[x].append(dom_wl)

        # add dominant wavelength as long as the distance to the neighbour shrinks with doing it
        if y > 0:
            while distance(thickness_values[x][y - 1], thickness_values[x][y] + dom_wl) < distance(
                    thickness_values[x][y - 1], thickness_values[x][y]):
                thickness_values[x][y] = thickness_values[x][y] + dom_wl
            while distance(thickness_values[x][y - 1], thickness_values[x][y] - dom_wl) < distance(
                    thickness_values[x][y - 1], thickness_values[x][y]):
                thickness_values[x][y] = thickness_values[x][y] - dom_wl
        if x > 0:
            while distance(thickness_values[x - 1][y], thickness_values[x][y] + dom_wl) < distance(
                    thickness_values[x - 1][y], thickness_values[x][y]):
                thickness_values[x][y] = thickness_values[x][y] + dom_wl
            while distance(thickness_values[x - 1][y], thickness_values[x][y] - dom_wl) < distance(
                    thickness_values[x - 1][y], thickness_values[x][y]):
                thickness_values[x][y] = thickness_values[x][y] - dom_wl

for x in range(int(img_width)):
    for y in range(int(img_height)):
        if thickness_values[x][y] > 3000:
            print(x, ", ", y)
            thickness_values[x][y] = 500

print(2)

# prepare plot
plt.style.use('_mpl-gallery')
X = np.arange(0, stop=int(img_width), dtype=int)
Y = np.arange(0, stop=int(img_height), dtype=int)
X, Y = np.meshgrid(X, Y)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, np.array(thickness_values))

plt.show()
