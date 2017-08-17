import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    lower_color = np.array([0, 0, 255  ])
    upper_color = np.array([255, 255, 255])

    mask = cv2.inRange(rgb, lower_color, upper_color)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('WebCam', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()