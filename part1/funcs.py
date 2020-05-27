from imageFunctions import *

img = makePicture('bear.jpg')
pixels = img.load()
setRed(img, 100, 100, 150)
setGreen(img, 100, 100, 0)
setBlue(img, 100, 100, 255)
show(img)
