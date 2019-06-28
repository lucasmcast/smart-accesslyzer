from tkinter import *
from PIL import Image
from PIL import ImageTk
from thread.VideoStream import VideoStream
from FacialRecognition import FacialRecognition
from arduino.ArduinoRead import ArduinoRead
from Ocorrencia import Ocorrencia
from thread.FPS import FPS
import cv2 as cv
import numpy as np
import os

class RecognizerTela:

    def __init__(self, master=None, video_source=0, numeroCanais=1):
        self.recognizer1 = FacialRecognition()
        self.recognizer2 = FacialRecognition()
        self.arduino = ArduinoRead().start()
        self.ocorrencia = Ocorrencia()
        
        self.nomeAnterior = ''
        self.statusAnterior = 0


        self.color_rect = self.recognizer1.COLOR_RECTANGLE
        self.color_text = self.recognizer1.COLOR_TEXT
        self.size_tex = self.recognizer1.SIZE_TEXT
        self.size_rect = self.recognizer1.SIZE_LINE_RECT
        self.font = self.recognizer1.FONT_TEXT

        self.fps = FPS().start()    

        self.window = master
        self.video_source = self.conexaoMultiCanal(video_source, numeroCanais)
        self.vid = MyVideoCapture(self.video_source)

        self.cord_x = 16
        self.cord_y = self.vid.height - 10

        self.primeiroContainer = Frame(self.window)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.window)
        self.segundoContainer["padx"] = 10
        self.segundoContainer.pack()
        
        self.canvas = Canvas(self.primeiroContainer, width=self.vid.width, height=self.vid.height)
        self.canvas.pack(side=LEFT)

        self.canvas1 = Canvas(self.primeiroContainer,width=self.vid.width, height=self.vid.height)
        self.canvas1.pack(side=RIGHT)

        self.canvas2 = Canvas(self.segundoContainer, width=self.vid.width, height=self.vid.height)
        self.canvas2.pack()

        self.delay = 15
        self.update()
        
        self.window.mainloop()
        
    def conexaoMultiCanal(self, video_source, numeroCanais):
        conexao = []
        for canal in range(1, numeroCanais + 1):
            conexao.append(video_source+"ch{}/main/av_stream".format(canal))
        return conexao
        

    def update(self):
        imagem = self.ocorrencia.person_picture[1]

        status = self.arduino.status_read()

        status1 = status[0]
        dxporta1 = status[1]

        frame1 = self.vid.get_frame(0)
        frame2 = self.vid.get_frame(1)

        frame1 = cv.resize(frame1, (self.vid.width, self.vid.height))
        frame2 = cv.resize(frame2, (self.vid.width, self.vid.height))

        self.recognizer1.face_recognize(frame1)
        self.recognizer2.face_recognize(frame2)

        cv.putText(frame1, status[2], (self.cord_x,self.cord_y), self.font, 1.0, status[3])

        detectou1 = self.recognizer1.detectou
        nome1 = self.recognizer1.nome

        detectou2 = self.recognizer2.detectou
        nome2 = self.recognizer2.nome

        e1, t1, d1, b1, texto1 = self.recognizer1.draw_object
        e2, t2, d2, b2, texto2 = self.recognizer2.draw_object

        if detectou1:
            print("0")
            cv.rectangle(frame1, (e1, t1), (d1, b1), self.color_rect, self.size_rect)
            cv.putText(frame1, texto1 , (e1, t1 -10),self.font, self.size_tex, self.color_text)
            if nome1 != "Desconhecido":
                imagem = cv.imread("db-faces/{}/01.jpg".format(nome1))
                imagem = cv.resize(imagem, (self.vid.width, self.vid.height))
        
        if detectou1 and self.nomeAnterior != nome1:
            print("1")
            self.ocorrencia.putOcorrencia(nome1, frame1)
            print(self.nomeAnterior)
            self.nomeAnterior = nome1
            cv.rectangle(frame1, (e1, t1), (d1, b1), self.color_rect, self.size_rect)
            cv.putText(frame1, texto1 , (e1, t1 -10),self.font, self.size_tex, self.color_text)

        if detectou2:
            print("0")
            cv.rectangle(frame2, (e2, t2), (d2, b2), self.color_rect, self.size_rect)
            cv.putText(frame2, texto2 , (e2, t2 -10),self.font, self.size_tex, self.color_text)
            if nome1 != "Desconhecido":
                imagem = cv.imread("db-faces/{}/01.jpg".format(nome2))
                imagem = cv.resize(imagem, (self.vid.width, self.vid.height))
        
        if detectou2 and self.nomeAnterior != nome2:
            print("1")
            self.ocorrencia.putOcorrencia(nome2, frame2)
            print(self.nomeAnterior)
            self.nomeAnterior = nome2
            cv.rectangle(frame2, (e2, t2), (d2, b2), self.color_rect, self.size_rect)
            cv.putText(frame2, texto2 , (e2, t2 -10),self.font, self.size_tex, self.color_text)

        if dxporta1 == 1:
            print("2")
            self.ocorrencia.save_img()
            if self.statusAnterior != dxporta1:
                self.statusAnterior = dxporta1
    
        if status1 == 1:
            self.statusAnterior = status1

        if status1 == 0 and self.statusAnterior == 1:
            print("3")
            self.ocorrencia.clean_ocorrencia()
            self.statusAnterior = status

        self.fps.update()
        self.fps.stop()
        textoFPS= str(int(self.fps.fps()))+" FPS"
        cv.putText(frame2, textoFPS , (10, 15),self.font, self.size_tex, self.color_text)

        self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame1))
        self.canvas.create_image(0,0, image=self.photo, anchor=NW)
        
        self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(frame2))
        self.canvas1.create_image(0,0,image=self.photo1, anchor=NW)

        self.photo2 = ImageTk.PhotoImage(image=Image.fromarray(imagem))
        self.canvas2.create_image(0,0,image=self.photo2, anchor=NW)

        self.window.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = []
        self.video_source = video_source
        self.initStreams()

        self.idx = 0
        
        self.width = int(self.vid[self.idx].get(cv.CAP_PROP_FRAME_WIDTH) / 2)
        self.height = int(self.vid[self.idx].get(cv.CAP_PROP_FRAME_HEIGHT) / 2)

    def initStreams(self):
        for idx, stream_canal in enumerate(self.video_source):
            self.vid.append(VideoStream(self.video_source[idx]))
            self.vid[idx].start()

            if not self.vid[idx].isOpened():
                raise ValueError("Não foi possivel abrir video", self.video_source)
            
        
        
    def get_frame(self, cam):
        
        if self.vid[cam].isOpened():
            frame = self.vid[cam].read()
            return cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        else:
            return None 

    def __del__(self):
        if self.vid[self.idx].isOpened():
            self.vid[self.idx].stop()


#101 = o primeiro numero se refere a o numero da cameras e os dois ultirmos é o tipo de stream        
tecvoz = "rtsp://admin:felix5803001234@10.35.27.9:554/Streaming/Channels"
cameraip = "rtsp://admin:felix5803001234@10.35.27.8:1026/Streaming/Channels/101"
hikvision = "rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/"


RecognizerTela(Tk(), hikvision, 2)