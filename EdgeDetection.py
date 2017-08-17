import cv2
# import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    edge = cv2.Canny(frame, 100, 170)

    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('edge', edge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()