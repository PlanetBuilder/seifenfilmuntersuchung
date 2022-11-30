from PIL import Image
import colour
import matplotlib.pyplot as plt
import numpy as np

img_width = 240
img_height = img_width

chromatic_stimulus = (0.3138, 0.3310)

img = Image.open("test.jpg", "r", None)
rgb_im = img.convert('RGB')

wavelengths = []


for x in range(int(img_width)):
    print(x)
    wavelengths.append([])
    for y in range(int(img_height)):
        wavelengths[x].append(colour.dominant_wavelength(colour.models.XYZ_to_xy(colour.sRGB_to_XYZ(rgb_im.getpixel((x, y)))), chromatic_stimulus)[0])
        if(y > 0):
            if wavelengths[x][y] - 200 > wavelengths[x][y-1]:
                wavelengths[x][y] = wavelengths[x][y] + 700

print(wavelengths)

plt.style.use('_mpl-gallery')

# Make data
X = np.arange(0, stop=int(img_width), dtype=int)
Y = np.arange(0, stop=int(img_height), dtype=int)
X, Y = np.meshgrid(X, Y)

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X, Y, np.array(wavelengths))

plt.show()
