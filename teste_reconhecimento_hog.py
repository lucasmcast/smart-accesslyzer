import cv2 as cv
import dlib
import numpy as np
import os
from thread import VideoStream
from facial_hog.facial_recognition import face_recognize
from arduino.ArduinoRead import ArduinoRead
import time

_dir = os.path.dirname(__file__)
dir_ocorrencias = os.path.join(_dir, "ocorrencias")

print(dir_ocorrencias)

def date_now_dia_mes_ano():
    result_time = time.localtime()
    date = "{}-{}-{}".format(result_time.tm_mday,result_time.tm_mon ,result_time.tm_year)
    return date

def date_now_full():
    result_time = time.localtime()
    date = "{}-{}-{}_{}:{}".format(result_time.tm_mday,result_time.tm_mon ,result_time.tm_year, result_time.tm_hour, result_time.tm_min)
    return date

cap = VideoStream(0).start()
ardu = ArduinoRead().start()

print(ardu.getPortasEmUso())

font = cv.FONT_HERSHEY_SIMPLEX
os.chdir("ocorrencias")
cord_x = 16
cord_y = 40
#cap = VideoStream("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/main/av_stream").start()
while True:

    frame = cap.read()
    status = ardu.status_read()
    #status01, dxporta1, texto1, color1, statu02, dxporta2, texto2, color2 = ardu.status_read()

    
    cv.putText(frame, status[2], (cord_x,cord_y), font, 1.0, status[3])
    cv.putText(frame, status[6], (cord_x,cord_y*2), font, 1.0, status[7])

    detectou, nome = face_recognize(frame)
    
    if detectou:
        if not os.path.exists(date_now_dia_mes_ano()):
            os.mkdir(date_now_dia_mes_ano())
        img_item = nome + date_now_full()+".png"
        cv.imwrite(img_item, frame)

    if status_anterior != status[0]:
        print("deu certo")
        
    status_anterior = status[0]

    cv.imshow("Frame", frame)
    if (cv.waitKey(1)  == ord('q')):
        img_item = "escuro.png"
        cv.imwrite(img_item, frame)
        break


cv.destroyAllWindows()
cap.stop()


