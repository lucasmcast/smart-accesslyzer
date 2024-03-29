import cv2 as cv
import numpy as np
import pickle
from thread.VideoStream import VideoStream

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.xml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
    labels = pickle.load(f)
    labels = {v:k for k,v in labels.items()}

cap = VideoStream(src=0).start()

while True:
    #captura frame por frame
    frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w] #yCord_start, xCord_end
        roi_color = frame[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf >= 45 and conf <= 85:
            print(conf)
            print(labels[id_])
            font = cv.FONT_HERSHEY_SIMPLEX
            name =  labels[id_]
            color = (255,0,0)
            stroke = 2
            cv.putText(frame, name, (x,y), font, 1, color, stroke, cv.LINE_AA)

        img_item = "my-image.png"
        cv.imwrite(img_item, frame)

        color = (0, 255, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (20,0,255), 2)

    #frame = cv.resize(frame, (320, 240))

    cv.imshow("Frame", frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cap.stop()
cv.destroyAllWindows()
