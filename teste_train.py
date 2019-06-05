from thread.VideoStream import VideoStream
import cv2
from facial_hog.facial_recognition import face_recognize
import dlib
from FacialRecognition import FacialRecognition
from thread.VideoShow import VideoShow
from thread.FileVideoStream import FileVideoStream
import numpy as np
from thread.FPS import FPS

recognize = FacialRecognition()
print("[INFO] executando THREAD frames com reconhecimento facial...")
#print("[INFO] executando NORMAL frames com reconhecimento facial...")
#rtsp://user:password@ip:porta/h264/ch1/main/av_stream
cap = VideoStream("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/main/av_stream").start()
#cap = VideoStream("rtsp://admin:felix5803001234@10.35.27.9:554/h264/ch5/main/av_stream", cv2.CAP_FFMPEG).start()
#cap = cv2.VideoCapture("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/main/av_stream")
#VideoShow(cap).start()
fps = FPS().start()
#cap = VideoStream().start()


largura = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#print(largura)              
winName = 'Janela de Teste para o SOPT'
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


while True:

    frame = cap.read()
    #print(frame.shape)

    #frame = cv2.resize(frame, (450,320))
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame = np.dstack([frame, frame, frame])
    frame = cv2.resize(frame, (int(largura/2), int(altura/2)))
    #print(frame.shape)
    recognize.face_recognize(frame)
    detectou = recognize.detectou
    e, t, d, b, texto = recognize.draw_object
    if detectou:
        cv2.rectangle(frame, (e, t), (d, b), color_rect, size_rect)
        cv2.putText(frame, texto , (e, t -10),font, size_tex, color_text)
    
    #face_recognize(frame)
    
    #out.write(frame)
    #fatia = frame[0:150, 150:300]
    fps.update()
    fps.stop()
    textoFPS= str(int(fps.fps()))+" FPS"
    cv2.putText(frame, textoFPS , (10, 15),font, size_tex, color_text)

    cv2.imshow(winName, frame)
    if cv2.waitKey(1) == 27:
        break

   
   

print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print("[INFO] Resolução: {}x{}".format(int(largura/2), int(altura/2)))
#cap.release()
cap.stop()
cv2.destroyAllWindows()


