from PIL import Image
import math


# 70 levels of gray
gscale1 = '"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`". '
# 10 levels of gray
gscale2 = "@%#*+=-:. "

image = Image.open('test.JPG').convert('L')
W,H = image.size[0],image.size[1]


print(W,H)