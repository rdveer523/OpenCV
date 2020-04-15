# https://docs.opencv.org/master/dc/d2e/tutorial_py_image_display.html
#---------------------------------------------------------------------

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# NOTE = RSTD (read, show, waitKey, destroy)

i1 = cv.imread(r"E:\Storage---OLD(20200329)\9---PROJ___7\2-PROJ___opencv\2---my_opencv_work\images\meinpuneiiser.jpg",0)
plt.imshow(i1, cmap="Accent", interpolation="bicubic")
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
