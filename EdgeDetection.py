import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)
i  = 0
while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    edge = cv2.Canny(frame, 100, 170)

    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('edge', edge)



    cv2.exp(frame, '~/Desktop/yu/lk.jpg')
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
time.sleep(5)
cap.release()
cv2.destroyAllWindows()