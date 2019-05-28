import dlib
#from thread import VideoStream
import cv2 as cv

detector = dlib.get_frontal_face_detector()
detector_pontos_faciais = dlib.shape_predictor("facial-hog/recursos/shape_predictor_68_face_landmarks.dat")
cap = cv.VideoCapture("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/main/av_stream")
#cap = cv.VideoCapture(0)
fonte = cv.FONT_HERSHEY_COMPLEX_SMALL

def imprime_pontos(imagem , pontos_faciais):
    for p in pontos_faciais.parts():
        cv.circle(frame, (p.x, p.y), 2, (0, 255, 0), thickness=-1)

def imprime_numeros(imagem, pontos_faciais):
    for i, p in enumerate(pontos_faciais.parts()):
        cv.putText(imagem, str(i), (p.x, p.y), fonte, .55, (0,0,255), 1)

while True:

    ret, frame = cap.read()
    frame = cv.flip(frame, 180)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    dets = detector(gray, 1)

    color = (0,255,0)
    for face in dets:
        e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
        pontos = detector_pontos_faciais(frame, face)
        imprime_pontos(frame, pontos)
        cv.rectangle(frame, (e, t), (d, b), color, 2)
     
    cv.imshow("Frame", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        img_file = "detector_face.png"
        cv.imwrite(img_file, frame)
        break

cv.destroyAllWindows()
cap.stop()