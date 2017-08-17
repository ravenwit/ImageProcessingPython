import cv2

cap = cv2.VideoCapture(0)
moving = cv2.createBackgroundSubtractorMOG2()

while True:
    _, frame = cap.read()
    moving = moving.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('Moving', moving)

    k = cv2.waitKey(30) & 0xFF
    if k == 27: break


cap.release()
cv2.destroyAllWindows()
