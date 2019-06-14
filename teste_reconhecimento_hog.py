import cv2 as cv
import numpy as np
from thread import VideoStream
from thread.VideoShow import VideoShow
from FacialRecognition import FacialRecognition
from arduino.ArduinoRead import ArduinoRead
from Ocorrencia import Ocorrencia
from thread.FPS import FPS

ocorrencia = Ocorrencia()
recognize = FacialRecognition()
#arduino = ArduinoRead().start()
#print("[INFO]: Arduino conectado com Sucesso")

cap1 = VideoStream("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/sub/av_stream").start()
#cap = VideoStream("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/sub/av_stream").start()
#show = VideoShow(cap1).start()

largura = int(cap1.get(cv.CAP_PROP_FRAME_WIDTH))
altura = int(cap1.get(cv.CAP_PROP_FRAME_HEIGHT))
print(altura, largura)

winName = 'Janela de Teste para o SOPT'
cv.namedWindow(winName, cv.WINDOW_NORMAL)
cv.setWindowProperty(winName, 2000, 2000)

#print(arduino.getPortasEmUso())

color_rect = recognize.COLOR_RECTANGLE
color_text = recognize.COLOR_TEXT
size_tex = recognize.SIZE_TEXT
size_rect = recognize.SIZE_LINE_RECT
font = recognize.FONT_TEXT

cord_x = 16
cord_y = 40

nomeAnterior = ''

fps = FPS().start()
while True:

    frame = cap.read()
    frame1 = cap1.read()

    frame1 = cv.resize(frame1, (largura, altura))
    
    all_imgs = np.concatenate((frame, frame1), axis=1)

    #status = arduino.status_read()
    #[0]status01, [1]dxporta1, [2]texto1, [3]color1, [4]statu02, [5]dxporta2, [6]texto2, [7]color2

    #status1 = status[0]
    #dxporta1 = status[1]
    
    #cv.putText(frame, status[2], (cord_x,cord_y), font, 1.0, status[3])
    #cv.putText(frame1, status[2], (cord_x,cord_y), font, 1.0, status[3])
    #cv.putText(frame, status[6], (cord_x,cord_y*2), font, 1.0, status[7])

    recognize.face_recognize(all_imgs)
    detectou = recognize.detectou
    nome = recognize.nome

    if detectou and nomeAnterior != nome:
        ocorrencia.putOcorrencia(nome, all_imgs)
        print(nomeAnterior)
        nomeAnterior = nome

    #if dxporta1 == 1:
    #ocorrencia.save_img()
    
    

    fps.update()
    fps.stop()
    textoFPS= str(int(fps.fps()))+" FPS"
    cv.putText(frame, textoFPS , (largura - 100, altura - 15),font, size_tex, color_text)

    cv.imshow(winName, all_imgs)
    if (cv.waitKey(1)  == ord('q')):
        ocorrencia.save_img()


cv.destroyAllWindows()
cap.stop()


