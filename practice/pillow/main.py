from PIL import Image

img = Image.open('ship1.jpg')
print(img.size)
print(img.format)
img.show()

r, g, b, = img.split()
r.show()
g.show()
b.show()