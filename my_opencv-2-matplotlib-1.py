# https://docs.opencv.org/master/dc/d2e/tutorial_py_image_display.html
#---------------------------------------------------------------------
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# with matplotlib
#====================
m1 = cv.imread(r"E:\Storage---OLD(20200329)\9---PROJ___7\2-PROJ___opencv\2---my_opencv_work\images\meinpuneiiser.jpg")
# without 0-zero, the image is in bluish and color
# with 0-zero, the image will be in complete green
"""
here you changing the color type cmap="...",
the first point is you should put 0 in the imread(),
then only the changes can occur in the image otherwise not
for more changes look at the below possible values
Color image loaded by OpenCV is in BGR mode.
But Matplotlib displays in RGB mode. So color images will not be displayed
correctly in Matplotlib if image is read with OpenCV.
Please see the exercises for more details.
"""
#cv.imshow("me in Pune-2019", m1)
plt.imshow(m1)#, cmap="winter", interpolation="bicubic")
# ValueError: Colormap color is not recognized.

# to hide tick values on X, Y axis
plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()

"""
Possible values in cmap are:
----------------------------
Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r,
CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys,Greys_r,
OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1,
Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r,
PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r,
RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r,
Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu,
YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r,
autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r,
cividis, cividis_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r,
cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray,
gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow,
gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot,
gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r,
inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, nipy_spectral_r,
ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow,
rainbow_r, seismic, seismic_r, spring, spring_r, summer, summer_r, tab10,
tab10_r, tab20, tab20_r, tab20b, tab20b_r, tab20c, tab20c_r, terrain,
terrain_r, twilight, twilight_r, twilight_shifted, twilight_shifted_r, viridis,
viridis_r, winter, winter_r
"""
