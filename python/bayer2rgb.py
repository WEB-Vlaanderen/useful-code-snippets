#!/usr/bin/env python

"""bayer2rgb.py : Script to conver BayerBG to RGB and store new video"""

__author__      = "Maarten Slembrouck"
__copyright__   = "Copyright 2021, Ghent"

#example
# python3 bayer2rgb.py -i "in.avi" -o "out.avi"

import cv2
import argparse

parser = argparse.ArgumentParser(description='Convert Bayer BG to RGB')
parser.add_argument('-i', '--input', type=str, required=True, help='input video')
parser.add_argument('-o', '--output', type=str, required=True, help='output video')

args = parser.parse_args()

fps = 20

cap = cv2.VideoCapture(args.input)
vw = None

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    h, w, channels = frame.shape
    #print(w,h)
    if vw is None:
        fourcc = cv2.VideoWriter_fourcc('F','M','P','4')
        vw = cv2.VideoWriter(args.output, fourcc, fps, (w, h))
    # Our operations on the frame come here
    if channels == 3:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
    vw.write(rgb)
    # Display the resulting frame
    ''' cv2.imshow('frame', rgb)
    if cv2.waitKey(1) == ord('q'):
        break'''
# When everything done, release the capture
cap.release()
vw.release()
cv2.destroyAllWindows()
