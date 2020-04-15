# https://gist.github.com/pknowledge/b8ba734ae4812d78bba78c0a011f0d46
#----------------------------------------------------------------------
import cv2

face_cascade = cv2.CascadeClassifier(r"E:\Storage---OLD(20200329)\9---PROJ___7\2-PROJ___opencv\2---my_opencv_work\facedetect\facexml\haarcascade_frontalface_default.xml")

#---------------------------------------------------------
# the below code is for face detection from images only
# Read the input image
img = cv2.imread(r"E:\Storage---OLD(20200329)\9---PROJ___7\2-PROJ___opencv\2---my_opencv_work\images\meinpune.jpg",0)
# convert into GRAY
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(img,1.1,4)
# rectangle
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h), (255,0,0),3)

# display
cv2.imshow("detection...",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
