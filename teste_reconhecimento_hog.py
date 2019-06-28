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
cap1 = VideoStream("rtsp://admin:felix5803001234@10.35.27.9:554/Streaming/Channels/101")
#cap1 = VideoStream()
cap1.start()
#cap = VideoStream("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/sub/av_stream").start()
#show = VideoShow(cap1).start()

largura = int(cap1.get(cv.CAP_PROP_FRAME_WIDTH) / 2)
altura = int(cap1.get(cv.CAP_PROP_FRAME_HEIGHT) / 2)
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
    frame1 = cap1.read()

    #frame1 = cv.resize(frame1, (largura, altura))
    
    #all_imgs = np.concatenate((frame1, frame1), axis=1)

    #status = arduino.status_read()
    #[0]status01, [1]dxporta1, [2]texto1, [3]color1, [4]statu02, [5]dxporta2, [6]texto2, [7]color2

    #status1 = status[0]
    #dxporta1 = status[1]
    
    #cv.putText(frame, status[2], (cord_x,cord_y), font, 1.0, status[3])
    #cv.putText(frame1, status[2], (cord_x,cord_y), font, 1.0, status[3])
    #cv.putText(frame, status[6], (cord_x,cord_y*2), font, 1.0, status[7])
    """
    recognize.face_recognize(frame1)
    detectou = recognize.detectou
    nome = recognize.nome

    e, t, d, b, texto = recognize.draw_object

    if detectou:
        cv.rectangle(frame1, (e, t), (d, b), color_rect, size_rect)
        cv.putText(frame1, texto , (e, t -10),font, size_tex, color_text)
    
    

    fps.update()
    fps.stop()
    textoFPS= str(int(fps.fps()))+" FPS"
    cv.putText(frame1, textoFPS , (largura - 100, altura - 15),font, size_tex, color_text)
"""
    cv.imshow(winName, frame1)
    if (cv.waitKey(1)  == ord('q')):
        img = frame1
        img_item = "fpsrecognize.png"
        cv.imwrite(img_item, img)
        break


cv.destroyAllWindows()
cap1.stop()


