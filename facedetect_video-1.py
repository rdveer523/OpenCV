# https://gist.github.com/pknowledge/b8ba734ae4812d78bba78c0a011f0d46
#----------------------------------------------------------------------
import cv2, time

fc = cv2.CascadeClassifier(r"E:\Storage---OLD(20200329)\9---PROJ___7\2-PROJ___opencv\2---my_opencv_work\facedetect\facexml\haarcascade_frontalface_default.xml")

# this cap code is for VIDEO
vd = cv2.VideoCapture(0)


a1=0
#while cap.isOpened():
while True:
    #create frame
    a1=a1+1
    #_, img = vd.read()
    ck, fr = vd.read()
    #print(ck)
    #print(fr)
    gray = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
    faces = fc.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces:
        cv2.rectangle(fr, (x,y), (x+w, y+h), (255, 0 , 0), 3)

    # Display the output
    cv2.imshow('img', fr)
    #cv2.imshow("is On...",gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vd.release()
cv2.destroyAllWindows()
