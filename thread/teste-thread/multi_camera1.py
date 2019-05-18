import cv2
import numpy as np

camera1 = "rtsp://usuario:senha@dominio/ip:554/h264/ch1/main/av_stream"
camera2 = "rtsp://usuario:senha@dominio/ip:554/h264/ch2/main/av_stream"
camera3 = "rtsp://usuario:senha@dominio/ip:554/h264/ch3/main/av_stream"
camera4 = "rtsp://usuario:senha@dominio/ip:554/h264/ch4/main/av_stream"

names = [camera1, camera2, camera3, camera4]

cap = [cv2.VideoCapture(i) for i in names]

frames = [None] * len(names)
ret = [None] * len(names)
resize = [None] * len(names)


while True:

    for i,c in enumerate(cap):
        if c is not None:
            ret[i], frames[i] = c.read()

    for i,f in enumerate(frames):
        if ret[i] is True:
            resize[i] = cv2.resize(frames[i], (320,220))
            if frames[i] % 2 == 0:
                numpy_horizontal_row1 = np.hstack((frames[i], frames[1]))


    #cv2.imshow('Image panel', frames[0])
    #print(frames)
    """
    numpy_horizontal_row1 = np.hstack((frames[0], frames[1]))
    numpy_horizontal_row2 = np.hstack((frames[2], frames[3]))

    combined_images = np.concatenate((numpy_horizontal_row1, numpy_horizontal_row2), axis=0)
    """
