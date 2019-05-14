import cv2
from thread.VideoStream import VideoStream
import dlib
from threading import Thread
import numpy as np

print(dlib.__version__)
print(dlib.__file__)
print(cv2.__version__)

cap1 = VideoStream("rtsp://admin:felix333235@192.168.2.50:1025/Streaming/Channels/102/").start()
#cap = VideoStream(0).start()
detector = dlib.get_frontal_face_detector()

def draw_rectangle(frame, faces_detectadas):
    for i, d in enumerate(faces_detectadas):
        e, t , d , b = (int(d.left()), int(d.top()), int(d.right()), int(d.bottom()))

        cv2.rectangle(frame, (e, t), (d, b), (0,255,0), 2)

while True:

    #frame = cap.read()
    frame1 = cap1.read()

    #frame = cv2.resize(frame, (400, 320))
    frame1 = cv2.resize(frame1, (320, 240))

    faces_detectadas = detector(frame1, 1)
    #print("Faces detectadas {}".format(len(faces_detectadas)))

    draw_rectangle(frame1, faces_detectadas)

    #row_frame = np.hstack((frame, frame1))
    cv2.imshow("Imagem", frame1)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.stop()
cap1.stop()