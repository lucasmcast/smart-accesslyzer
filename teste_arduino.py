import serial
from arduino.ArduinoRead import ArduinoRead
from thread import VideoStream
import cv2 as cv
from thread.FPS import FPS

cap = VideoStream("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/main/av_stream")
cap.start()
print("[INFO1]: Teste com comunicação arduino e FPS thread ")
ardu = ArduinoRead().start()

font = cv.FONT_HERSHEY_SIMPLEX
largura = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
altura = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

cord_x = 16
cord_y = 40
fps = FPS().start()
while True:
        
    frame = cap.read()
    status = ardu.status_read()
    
    
    cv.putText(frame, status[2], (cord_x,cord_y), font, 1.0, status[3])
    cv.putText(frame, status[6], (cord_x,cord_y*2), font, 1.0, status[7])

    cv.imshow("Frame", frame)
    if (cv.waitKey(1) & 0xFF == 27):
        break
    fps.update()
    fps.stop()
    textoFPS= str(int(fps.fps()))+" FPS"
    cv.putText(frame, textoFPS , (10, altura -10),font, 1, (0,0,255))

cap.stop()
cap.join()
cv.destroyAllWindows()

    
    
    