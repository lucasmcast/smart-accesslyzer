import cv2
from threading import Thread

class VideoStream():

    def __init__(self, src=0):
        #inicializa o video da camera e le o primeiro frame do stream
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        #variavel utilizada para indicar se a thread foi parada
        self.stopped = False

    def update(self):
        #mantem o loop infinito ate a thread ser parada
        while not self.stopped:
            #if a variavel indicar verdadeiro a thread para
            if not self.grabbed:
                self.stop()
            else:
                #caso contrario optem o proximo quadro(frame)
                (self.grabbed, self.frame) = self.stream.read()

    def stop(self):
        #indica que a thread sera parada
        self.stopped = True

    def start(self):
        Thread(target=self.update, args=()).start()
        return self

    def read(self):
        #retorna o frame mais recente lido
        return self.frame

    #retorna a propriedade especifica do video
    def get(self, propid):
        return self.stream.get(propid)

    #define as propriedades do video
    def set(self, propid, value):
        self.stream.set(propid, value)
