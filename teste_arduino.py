import serial
from arduino.ArduinoRead import ArduinoRead
from thread import VideoStream
import cv2 as cv

cap = VideoStream().start()
ardu = ArduinoRead().start()

font = cv.FONT_HERSHEY_SIMPLEX

cord_x = 16
cord_y = 40
while True:
        
    frame = cap.read()
    dxporta1, texto1, color1, dxporta2, texto2, color2 = ardu.status_read()
    
    
    cv.putText(frame, texto1, (cord_x,cord_y), font, 1.0, color1)
    cv.putText(frame, texto2, (cord_x,cord_y*2), font, 1.0, color2)

    cv.imshow("Frame", frame)
    if (cv.waitKey(1) & 0xFF == ord('q')):
        break

cap.stop()
cv.destroyAllWindows()

    
    
    