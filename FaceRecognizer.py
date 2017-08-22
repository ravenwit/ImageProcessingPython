#!/usr/bin/env python

'''
face detection using haar cascades

USAGE:
    facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [--video-source <video_source>] [command]
        command: test, train, detect, recognize
'''

from __future__ import print_function

import cv2, time, sys, getopt

PATH = './train_data'


def detect(img, _cascade):
    _rects = _cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
    if len(_rects) == 0:
        return []
    _rects[:, 2:] += _rects[:, :2]
    return _rects


def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


if __name__ == '__main__':
    print(__doc__)

    args = getopt.getopt(sys.argv[1:], '', ['face-cascade=', 'eye-cascade=', 'identifier-cascades=', 'video-source='])
    # check parameters and set default value
    # each command will handle a function
    # get all xml file from train_data and load if recognise
    # loop the camera in main and forward the frame
