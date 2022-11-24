from PIL import Image, ImageDraw, ImageFont

img = Image.new("RGB", (1536, 1536))
for i in range(255):
    print((255, i, 0))
    for j in range(1536):
        img.putpixel((j, i), (255, i, 0))
for i in range(255):
    print((255-i, 255, 0))
    for j in range(1536):
        img.putpixel((j, i+255), (255-i, 255, 0))
for i in range(255):
    print((0, 255, i))
    for j in range(1536):
        img.putpixel((j, i+510), (0, 255, i))
for i in range(255):
    print((0, 255-i, 255))
    for j in range(1536):
        img.putpixel((j, i+765), (0, 255-i, 255))
for i in range(255):
    print((i, 0, 255))
    for j in range(1536):
        img.putpixel((j, i+1020), (i, 0, 255))
for i in range(255):
    print((255, 0, 255-i))
    for j in range(1536):
        img.putpixel((j, i+1275), (255, 0, 255-i))

img.show()