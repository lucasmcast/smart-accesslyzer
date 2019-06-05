import numpy as np
import cv2 as cv
import dlib


cap = cv.VideoCapture(0)
detector_face =  dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()

    faces_detectadas = detector_face(frame, 1)

    for face in faces_detectadas:
        e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
        print(e, t, d, b)
        #pts = np.array([[int(face.left()), int(face.top()) ], [int(face.top())], [int(face.right())], [int(face.bottom())]], np.int32)
        pts = np.array([[10,5], [10,20], [10 , 5], [20, 20]], np.int32)
        cv.polylines(frame, [pts], True, (0,255,0), 1)
    
    cv.imshow("Frame", frame)
    if cv.waitKey(1) == 27:
        break

cap.release()
cv.destroyAllWindows()      
