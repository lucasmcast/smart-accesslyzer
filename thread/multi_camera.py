import cv2
import numpy as np
from thread.VideoStream import VideoStream


video1 = VideoStream("rtsp://admin:felix333235@192.168.2.50:1025/Streaming/Channels/101/").start()
video2 = VideoStream("rtsp://admin:felix5803001234@189.114.223.154:554/h264/ch2/sub/av_stream").start()
video3 = VideoStream("rtsp://admin:felix5803001234@189.114.223.154:554/h264/ch3/sub/av_stream").start()
video4 = VideoStream("rtsp://admin:felix5803001234@189.114.223.154:554/h264/ch4/sub/av_stream").start()


while True:

    image1 = video1.read()
    image2 = video2.read()
    image3 = video3.read()
    image4 = video4.read()

    # Note all frames must be of the same size
    image1 = cv2.resize(image1, (320, 240))
    image2 = cv2.resize(image2, (320, 240))
    image3 = cv2.resize(image3, (320, 240))
    image4 = cv2.resize(image4, (320, 240))

    """
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
    """
    numpy_horizontal_row1 = np.hstack((image1, image2))
    numpy_horizontal_row2 = np.hstack((image3, image4))

    combined_images = np.concatenate((numpy_horizontal_row1, numpy_horizontal_row2), axis=0)

    cv2.imshow('Image panel', combined_images)
    if cv2.waitKey(1) == ord('q'):
        break

