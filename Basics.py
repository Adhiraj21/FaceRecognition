import cv2
import numpy as np
import face_recognition

imgRonaldo= face_recognition.load_image_file('train images/Ronaldo 1.jpg')
imgRonaldo = cv2.cvtColor(imgRonaldo,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('test images/Ronaldo 2.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgRonaldo)[0]
encodeRonaldo = face_recognition.face_encodings(imgRonaldo)[0]
cv2.rectangle(imgRonaldo,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)

facelocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(facelocTest[3],facelocTest[0]),(facelocTest[1],facelocTest[2]),(255,0,255),2)

results=face_recognition.compare_faces([encodeRonaldo],encodeTest)
faceDis = face_recognition.face_distance([encodeRonaldo],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('Cristiano Ronaldo',imgRonaldo)
cv2.imshow('Cristiano Test',imgTest)
cv2.waitKey(0)
