from threading import  Thread
import cv2
from thread import VideoStream
from FacialRecognition import FacialRecognition

class VideoShow():

    def __init__(self,  capture):
        self.capture = capture
        self.frame = None
        self.stopped = False
        self.recognize = FacialRecognition()
        self.show()
        

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        while not self.stopped:
            self.frame = self.capture.read()
            self.frame = cv2.resize(self.frame, (360,288))
            self.recognize.face_recognize(self.frame)
            cv2.imshow("Video", self.frame)
            cv2.waitKey(1)

    def stop(self):
        self.stopped = True

    def readFrame(self):
        return self.frame