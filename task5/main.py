import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('face.jpg')
img2 = cv2.imread('face2.jpg')
img3 = cv2.imread('face3.jpg')
img4 = cv2.imread('face4.jpg')
img5 = cv2.imread('face5.jfif')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=1, minSize=(10, 10))
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
cv2.imshow('face1',img)
cv2.waitKey(0)

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(10, 10))
for (x,y,w,h) in faces:
    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img2[y:y+h, x:x+w]
cv2.imshow('face2',img2)
cv2.waitKey(0)

gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10, minSize=(5, 5))
for (x,y,w,h) in faces:
    cv2.rectangle(img3,(x,y),(x+w,y+h),(0,0,255),3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img3[y:y+h, x:x+w]
cv2.imshow('face3',img3)
cv2.waitKey(0)

gray = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=1, minSize=(10, 10))
for (x,y,w,h) in faces:
    cv2.rectangle(img4,(x,y),(x+w,y+h),(0,0,255),3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img4[y:y+h, x:x+w]
cv2.imshow('face4',img4)
cv2.waitKey(0)

gray = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=20, minSize=(10, 10))
for (x,y,w,h) in faces:
    cv2.rectangle(img5,(x,y),(x+w,y+h),(0,0,255),3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img5[y:y+h, x:x+w]
cv2.imshow('face5',img5)
cv2.waitKey(0)

cv2.destroyAllWindows()