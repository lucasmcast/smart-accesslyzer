import os
import cv2 as cv
import pickle as cPickle
import numpy as np
from PIL import Image
import dlib
from thread.VideoStream import VideoStream

detector_face = dlib.get_frontal_face_detector()
detector_pontos = dlib.shape_predictor("recursos/shape_predictor_68_face_landmarks.dat")
reconhecimento_facial = dlib.face_recognition_model_v1("recursos/dlib_face_recognition_resnet_model_v1.dat")

indices = np.load("indices.pickle")
descritores_faciais = np.load("descritores.npy")

#variavel responsavel por filtrar valores a baixo do ideal/precisão no reconhecimento
limiar = 0.5

cap = VideoStream("rtsp://admin:felix5803001234@10.35.27.9:554/h264/ch5/main/av_stream").start()

while True:

    frame = cap.read()
    faces_detectadas = detector_face(frame, 0)

    for face in faces_detectadas:
        e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
        pontos_faciais = detector_pontos(frame, face)

        descritor_facial = reconhecimento_facial.compute_face_descriptor(frame, pontos_faciais)

        lista_descritor_facial = [fd for fd in descritor_facial]

        np_array_descritor_facial = np.asarray(lista_descritor_facial, dtype=np.float64)
        np_array_descritor_facial = np_array_descritor_facial[np.newaxis, :]

        distancias = np.linalg.norm(np_array_descritor_facial - descritores_faciais, axis=1)

        minimo = np.argmin(distancias)

        distancia_minima = distancias[minimo]

        if distancia_minima <= limiar:
            nome = os.path.split(indices[minimo])[1].split(".")[0]
        else:
            nome = " "

        cv.rectangle(frame, (e, t), (d, b), (0, 255, 255), 2)
        texto = "{} {:.4f}".format(nome, distancia_minima)
        cv.putText(frame, texto, (d, t), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0, 255, 255))


    cv.imshow("Frame", frame)
    if (cv.waitKey(1) & 0xFF == ord('q')):
        break

cap.stop()
cv.destroyAllWindows()


