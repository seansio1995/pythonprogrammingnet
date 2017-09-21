from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean


def threshold(imageArray):
    resArray=[]
    for pixelRow in imageArray:
        for pixel in pixelRow:
            avgPixel=mean(pixel[:3])
            resArray.append(avgPixel)
    balance=mean(resArray)

    newArray=imageArray
    for pixelRow in newArray:
        for pixel in pixelRow:
            if mean(pixel[:3]) > balance:
                pixel[0]=255
                pixel[1]=255
                pixel[2]=255
            else:
                pixel[0]=0
                pixel[1]=0
                pixel[2]=0

    return newArray

i = Image.open('images/numbers/0.1.png')
iar = np.array(i)
i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)
i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)
i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)


iar = threshold(iar)
iar2 = threshold(iar2)
iar3 = threshold(iar3)
iar4 = threshold(iar4)

fig = plt.figure()
ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()
