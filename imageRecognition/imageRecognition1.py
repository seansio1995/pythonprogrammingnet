from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# i=Image.open("images/dot.png")
# print(np.asarray(i))

# i2=Image.open("images/dotndot.png")
# #print(np.asarray(i2))
# i2array=np.asarray(i2)
# plt.imshow(i2array)
# plt.show()
#
#
# iarray=np.asarray(Image.open("images/dot.png"))
# plt.imshow(iarray)
# plt.show()


i = Image.open('images/numbers/y0.4.png')
iar=np.asarray(i)

plt.imshow(iar)
print(iar)
# print(iar)
plt.show()
