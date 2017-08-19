import cv2
import numpy as np

face_casacde = cv2.CascadeClassifier('face.xml')

eye_cascade = cv2.CascadeClassifier('eye.xml')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_casacde.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        rec_gray = gray[y:y+h, x:x+w]
        rec_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(rec_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(rec_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow('Video', frame)
