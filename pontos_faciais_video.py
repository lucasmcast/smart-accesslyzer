import dlib
import cv2
import numpy as np
from thread.VideoStream import VideoStream

fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL

def imprime_pontos(imagem , pontos_faciais):
    for p in pontos_faciais.parts():
        cv2.circle(frame, (p.x, p.y), 1, (0, 255, 0), thickness=-1)

def imprime_numeros(imagem, pontos_faciais):
    for i, p in enumerate(pontos_faciais.parts()):
        cv2.putText(imagem, str(i), (p.x, p.y), fonte, .55, (0,0,255), 1)

def imprime_linhas(imagem, pontos_faciais):
    p68 = [[0,16, False], #linha do queixo
           [17, 21, False], #sobranceira direita
           [22, 26, False], #sobranceira esquerda
           [27, 30, False], #ponte nasal
           [30, 35, True], #nariz inferior
           [36, 41, True], #olho esquerdo
           [42, 47, True], #olho direito
           [48, 59, True], #labio externo
           [60, 67, True]] #labio interno
    for k in range(0, len(p68)):
        pontos = []
        for i in range(p68[k][0], p68[k][1] + 1):
            ponto = [pontos_faciais.part(i).x, pontos_faciais.part(i).y]
            pontos.append(ponto)
        pontos = np.array(pontos, dtype=np.int32)
        cv2.polylines(imagem, [pontos], p68[k][2], (255, 0, 0), 2)

video_cap = VideoStream(0).start()
detector_face =  dlib.get_frontal_face_detector()
detector_pontos_faciais = dlib.shape_predictor("facial-hog/recursos/shape_predictor_68_face_landmarks.dat")
#taxa de mudança de frame
#video_cap.set(cv2.CAP_PROP_FPS, 30)
#Resolução
#video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while (not video_cap.stopped):


    frame = video_cap.read()
    #vira o video em 180ª
    frame = cv2.flip(frame, 180)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    #clahe_image = clahe.apply(gray)


    faces_detectadas = detector_face(gray, 1)

    for face in faces_detectadas:
        pontos = detector_pontos_faciais(frame, face)
        imprime_pontos(frame, pontos)
        #imprime_numeros(frame, pontos)
        #imprime_linhas(frame, pontos)

    #cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.imshow("image", frame) #Display the frame

    #altura, largura, fps = video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT), video_cap.get(cv2.CAP_PROP_FRAME_WIDTH), \
                           #video_cap.get(cv2.CAP_PROP_FPS)

    #print(altura, largura, fps)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit program when the user presses 'q'
        break

video_cap.stop()
cv2.destroyAllWindows()

