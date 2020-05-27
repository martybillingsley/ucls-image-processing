from imageFunctions import *

def drawRedLine():
    for x in range(getWidth(img)):
        setRed(img, x, 100, 255)
        setGreen(img, x, 100, 0)
        setBlue(img, x, 100, 0)


img = makePicture('bear.jpg')
pixels = img.load()
drawRedLine()
show(img)
