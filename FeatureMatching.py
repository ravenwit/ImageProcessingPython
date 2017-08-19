import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('redstapler.png', 1)
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(img, None)
    kp2, des2 = orb.detectAndCompute(frame, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)
    matches = sorted(matches, key= lambda x: x.distance)

    res = cv2.drawMatches(img, kp1, frame, kp2, matches[:30], None, flags=2)
    plt.imshow(res)
    plt.show()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
