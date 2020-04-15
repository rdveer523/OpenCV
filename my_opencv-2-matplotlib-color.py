import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# NOTE: here don't mention 0 in imread() because you will have a ValueError
# ValueError: not enough values to unpack (expected 3, got 1)
a1 = cv.imread(r"E:\Storage---OLD(20200329)\9---PROJ___7\2-PROJ___opencv\2---my_opencv_work\images\meinpuneiiser.jpg")

#-------------------------
#b,g,r = cv.split(a1)
#a2 = cv.merge([r,g,b])
a2 = a1[:,:,::-1]
# the above code represents the matrix formation of an image
print(a1[:])

plt.subplot(121);plt.imshow(a1)
plt.subplot(122);plt.imshow(a2)
plt.show()

#--------------------------

#cv.imshow("original",a1)
#cv.imshow("modified",a2)
# the above two lines displays the images individually

cv.waitKey(0)
cv.destroyAllWindows()
