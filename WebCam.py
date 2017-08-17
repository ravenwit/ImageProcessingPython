import cv2
import time
import os
# import numpy as np


FOLDER = 'caps'
TIME = 50
PATH = os.path.join(os.path.expanduser('~/'), FOLDER)
if not os.path.exists(PATH):
    os.makedirs(PATH)


cap = cv2.VideoCapture(0)
c = 0
start_time = int(time.time())


while True:
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Webcam', frame)
    # cv2.imshow('Webcam Analysis', gray)
    cur_time = int(time.time())
    c += 1
    cv2.imwrite(os.path.join(PATH, 'cap-{}.png'.format(c)), frame)
    if cur_time - start_time == TIME:
        break
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
print(c/TIME)
cap.release()
cv2.destroyAllWindows()

