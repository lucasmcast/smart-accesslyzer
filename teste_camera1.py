from thread.VideoStream import VideoStream
import cv2
from facial_hog.facial_recognition import face_recognize
import dlib
from FacialRecognition import FacialRecognition
from thread.FileVideoStream import FileVideoStream
import numpy as np
from thread.FPS import FPS
from Ocorrencia import Ocorrencia
from arduino.ArduinoRead import ArduinoRead


ocorrencia = Ocorrencia()
arduino = ArduinoRead().start()
#cap = VideoStream("rtsp://admin:felix5803001234@10.35.27.9:554/Streaming/Channels/01")
cap = VideoStream("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/main/av_stream")
#cap = VideoStream(0)
cap.start()
#cap = VideoStream(0).start()
recognize = FacialRecognition()
print("[INFO] executando THREAD frames com reconhecimento facial...")




largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) / 2)
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) / 2)
winName = 'Janela de Teste para 1 Câmera'
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(winName, 2000, 2000)

# Define the codec and create VideoWriter objectcle
#fourcc = cv2.VideoWriter_fourcc(*'H264')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(altura),int(largura)))

color_rect = recognize.COLOR_RECTANGLE
color_text = recognize.COLOR_TEXT
size_tex = recognize.SIZE_TEXT
size_rect = recognize.SIZE_LINE_RECT
font = recognize.FONT_TEXT
nomeAnterior = ''
statusAnterior = 0

cord_x = 16
cord_y = altura - 10
fps = FPS().start()
while True:

    frame = cap.read()
    status = arduino.status_read()
    
    status1 = status[0]
    dxporta1 = status[1]
    
    frame = cv2.resize(frame, (largura, altura))
    recognize.face_recognize(frame)
    
    cv2.putText(frame, status[2], (cord_x,cord_y), font, 1.0, status[3])
    #cv2.putText(frame, status[6], (cord_x,cord_y*2), font, 1.0, status[7])

    detectou = recognize.detectou
    nome = recognize.nome

    e, t, d, b, texto = recognize.draw_object

    if detectou:
        cv2.rectangle(frame, (e, t), (d, b), color_rect, size_rect)
        cv2.putText(frame, texto , (e, t -10),font, size_tex, color_text)
    
    if detectou and nomeAnterior != nome:
        ocorrencia.putOcorrencia(nome, frame)
        print(nomeAnterior)
        nomeAnterior = nome
        cv2.rectangle(frame, (e, t), (d, b), color_rect, size_rect)
        cv2.putText(frame, texto , (e, t -10),font, size_tex, color_text)

    if dxporta1 == 1:
        ocorrencia.save_img()
        if statusAnterior != dxporta1:
            statusAnterior = dxporta1
    if status1 == 1:
        statusAnterior = status1
        
    if status1 == 0 and statusAnterior == 1:
        ocorrencia.clean_ocorrencia()
        statusAnterior = status

    
    fps.update()
    fps.stop()
    textoFPS= str(int(fps.fps()))+" FPS"
    cv2.putText(frame, textoFPS , (10, 15),font, size_tex, color_text)

    cv2.imshow(winName, frame)
    if cv2.waitKey(1) == 27:
        break  

print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print("[INFO] Resolução: {}x{}".format(largura, altura))

cap.stop()
cap.join()
cv2.destroyAllWindows()


