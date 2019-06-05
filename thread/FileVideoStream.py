import cv2 as cv
from queue import Queue
from threading import Thread

class FileVideoStream():

    def __init__(self, path=0, queueSize=128):
        self.stream = cv.VideoCapture(path)
        self.grabbed, self.frame = self.stream.read()
        self.stopped = False

        self.Q = Queue(maxsize =queueSize)

    def start(self):
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self
    
    def update(self):
        while True:
            if self.stopped:
                return
            
            if not self.Q.full():
                (self.grabbed, self.frame) = self.stream.read()

                if not self.grabbed:
                    self.stop()
                    return

                self.Q.put(self.frame)
                
    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True
