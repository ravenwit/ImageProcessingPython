#!/usr/bin/env python

'''
face detection using haar cascades

USAGE:
    FaceRecognizer.py [--cascades, -c <"cascade list or directory containing cascades in yml extensions">] [--video-source <video_source>] [command]
        command: test, train, detect, recognize
'''

from __future__ import print_function

import cv2, time, sys, getopt, os

PATH = './train_data'


def __get_cascades(elements):
    elements = elements.split(',')
    cascades = []
    for element in elements:
        element = os.path.abspath(element)
        if not os.path.exists(element):
            re_element = os.path.abspath(os.getcwd() + element)
            if not os.path.exists(re_element):
                print('Neither {} or {} exist.'.format(element, re_element))
                continue
            else:
                element = re_element
        if os.path.isfile(element) and element.lower().endswith('.yml'):
            cascades.append(element)
        elif os.path.isdir(element):
            items = os.listdir(element)
            for item in items:
                item_path = os.path.abspath(os.path.join(element, item))
                if os.path.isfile(item_path) and item.lower().endswith('.yml'):
                    cascades.append(item_path)
    return cascades


def _get_opts():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'c:s:', ['cascades=', 'video-source=', 'detect', 'train', 'recognize'])
        if opts is None and args is None:
            raise getopt.GetoptError
    except getopt.GetoptError as err:
        # print error information
        print(str(err))
        # print help information
        print(__doc__)
        # Exit
        sys.exit(2)

    command = None
    cascades = None
    video_source = None

    if args:
        command = args[0].lower()

    if command not in ('detect', 'train', 'recognize'):
        print(__doc__)
        command = 'test'

    for o, el in opts:
        if o in ('-c', '--cascades'):
            cascades_element = el
            cascades = __get_cascades(cascades_element)
            if cascades is None or not cascades:
                print("No cascade is given or given cascades do not exist.")
                command = 'test'
        elif o in ('-s', '--video-source'):
            try:
                video_source = int(el)
            except ValueError as err:
                print('Video source must be an integer. \nSetting video source to default value 0')
                video_source = 0
        else:
            print(__doc__)

    return video_source, command, cascades


def _detect(img, _cascade):
    _rects = _cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
    if len(_rects) == 0:
        return []
    _rects[:, 2:] += _rects[:, :2]
    return _rects


def _draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


if __name__ == '__main__':
    vs, command, cascades = _get_opts()
    print(vs)
    print(command)
    print(cascades)
