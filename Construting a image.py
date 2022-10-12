
from PIL import Image
imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))

# drawing area
xa = -1.0
xb = 1.0
ya = -1.0
yb = 1.0

for y in range(imgy):
    for x in range(imgx):
        image.putpixel((x,y), (int(x)**2,int(y),0))

image.save("test.png", "PNG")
