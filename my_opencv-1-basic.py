# https://docs.opencv.org/master/dc/d2e/tutorial_py_image_display.html
#---------------------------------------------------------------------

import cv2 as cv
import numpy as np


# Loads a default image. Any transparency of image will be neglected.
i1 = cv.imread(r"E:\Storage---OLD(20200329)\9---PROJ___7\2-PROJ___opencv\2---my_opencv_work\images\meinpuneiiser.jpg",0)
#i1 = cv.imread(r"E:\0_______1-OpenCV\1---my_opencv_work\meinpune.jpg",cv.IMREAD_COLOR)

# Loads image in grayscale mode
#i2 = cv.imread(r"E:\0_______1-OpenCV\1-my_opencv_work\meinpuneiiser.jpg",0)
#i2 = cv.imread(r"E:\0_______1-OpenCV\1---my_opencv_work\meinpune.jpg",cv.IMREAD_GRAYSCALE)

# Loads image as such including alpha channel
#i3 = cv.imread(r"E:\0_______1-OpenCV\1---my_opencv_work\meinpune.jpg",cv.IMREAD_UNCHANGED)

"""
# Even if the image path is wrong, it won't throw any error, but
# print img will give you None like below because you have not mentioned
# any value in the abve code after the path given
"""
cv.imshow("me in pune 2019...",i1)
#cv.imshow("Me in Pune IISER",i2)
#cv.imshow("Me in Pune IISER",i3)

# photo stays for 10 seconds = 10000 millisec
cv.waitKey(0)
# no time i.e stays until close from your side
#cv.waitKey(0)
cv.destroyAllWindows()
