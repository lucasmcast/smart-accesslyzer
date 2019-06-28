from tkinter import *
from PIL import Image
from PIL import ImageTk
from thread.VideoStream import VideoStream
from FacialRecognition import FacialRecognition
from Ocorrencia import *
from arduino.ArduinoRead import ArduinoRead
from thread.FPS import FPS
import cv2 as cv

class RecognizerTela:

    def __init__(self, master=None, video_source=0):
        self.recognizer = FacialRecognition()
        self.arduino = ArduinoRead().start()
        self.ocorrencia = Ocorrencia()
        
        self.nomeAnterior = ''
        self.statusAnterior = 0


        self.color_rect = self.recognizer.COLOR_RECTANGLE
        self.color_text = self.recognizer.COLOR_TEXT
        self.size_tex = self.recognizer.SIZE_TEXT
        self.size_rect = self.recognizer.SIZE_LINE_RECT
        self.font = self.recognizer.FONT_TEXT

        self.fps = FPS().start()    

        self.window = master
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)
        self.imagem = None

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

        self.delay = 15
        self.update()
        
        
        self.window.mainloop()
        

    def update(self):
        self.imagem = self.ocorrencia.person_picture[1]
        
        status = self.arduino.status_read()

        status1 = status[0]
        dxporta1 = status[1]

        frame = self.vid.get_frame()
        frame = cv.resize(frame, (self.vid.width, self.vid.height))
        
        self.recognizer.face_recognize(frame)

        cv.putText(frame, status[2], (self.cord_x,self.cord_y), self.font, 1.0, status[3])

        detectou = self.recognizer.detectou
        nome = self.recognizer.nome

        e, t, d, b, texto = self.recognizer.draw_object
        if detectou:
            print("0")
            cv.rectangle(frame, (e, t), (d, b), self.color_rect, self.size_rect)
            cv.putText(frame, texto , (e, t -10),self.font, self.size_tex, self.color_text)
            if nome != "Desconhecido":
                self.imagem = cv.imread("db-faces/{}/01.jpg".format(nome))
                self.imagem = cv.resize(self.imagem, (self.vid.width, self.vid.height))
      
        if detectou and self.nomeAnterior != nome:
            print("1")
            self.ocorrencia.putOcorrencia(nome, frame)
            print(self.nomeAnterior)
            self.nomeAnterior = nome
            cv.rectangle(frame, (e, t), (d, b), self.color_rect, self.size_rect)
            cv.putText(frame, texto , (e, t -10),self.font, self.size_tex, self.color_text)

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
        cv.putText(frame, textoFPS , (10, 15),self.font, self.size_tex, self.color_text)

        self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
        self.canvas.create_image(0,0, image=self.photo, anchor=NW)
        
        #self.imagem = cv.cvtColor(self.imagem, cv.COLOR_BGR2RGB)

        self.photo1 = ImageTk.PhotoImage(image=Image.fromarray(self.imagem))
        self.canvas1.create_image(0,0,image=self.photo1, anchor=NW)

        self.window.after(self.delay, self.update)

class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = VideoStream(video_source)
        self.vid.start()
        if not self.vid.isOpened():
            raise ValueError("Não foi possivel abrir video", video_source)
        
        self.width = int(self.vid.get(cv.CAP_PROP_FRAME_WIDTH) / 2)
        self.height = int(self.vid.get(cv.CAP_PROP_FRAME_HEIGHT) / 2)

    def get_frame(self):
        if self.vid.isOpened():
            frame = self.vid.read()
            return cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        else:
            return None 

    def __del__(self):
        if self.vid.isOpened():
            self.vid.stop()

#101 = o primeiro numero se refere a o numero da cameras e os dois ultirmos é o tipo de stream        
tecvoz = "rtsp://admin:felix5803001234@10.35.27.9:554/Streaming/Channels/1602"
cameraip = "rtsp://admin:felix5803001234@10.35.27.8:1026/Streaming/Channels/101"
hikvision = "rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/main/av_stream"

RecognizerTela(Tk(), hikvision)