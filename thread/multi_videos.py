import numpy as np
import cv2

camera1 = "rtsp://admin:felix5803001234@189.114.223.154:554/h264/ch1/main/av_stream"
camera2 = "rtsp://admin:felix5803001234@189.114.223.154:554/h264/ch2/main/av_stream"
camera3 = "rtsp://admin:felix5803001234@189.114.223.154:554/h264/ch3/main/av_stream"
camera4 = "rtsp://admin:felix5803001234@189.114.223.154:554/h264/ch4/main/av_stream"

names = [camera1, camera2, camera3, camera4]
window_titles = ['first', 'second', 'third', 'fourth']


cap = [cv2.VideoCapture(i) for i in names]

frames = [None] * len(names)
resize = [None] * len(names)
ret = [None] * len(names)

while True:

    for i,c in enumerate(cap):
        if c is not None:
            ret[i], frames[i] = c.read()


    for i,f in enumerate(frames):
        if ret[i] is True:
            resize[i] = cv2.resize(frames[i], (320,220))
            cv2.imshow(window_titles[i], resize[i])

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break


for c in cap:
    if c is not None:
        c.release();

cv2.destroyAllWindows()