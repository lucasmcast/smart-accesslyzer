"""
    Autor: Lucas Martins de Castro
    Data: 21/05/2019
    Descricao: Modolu responsavel por fazer o reconhecimento facial comparando
    as imagens do banco de dados ja treinadas.
"""

import cv2 as cv
import dlib
import numpy as np
import os

shape_predictor = "facial_hog/recursos/shape_predictor_68_face_landmarks.dat"
model_face_recognition = "facial_hog/recursos/dlib_face_recognition_resnet_model_v1.dat"
indices_dir = "facial_hog/recursos/indices.pickle"
descriptors_dir = "facial_hog/recursos/descritores.npy"

""" 
Carrega todos os arquivos necessarios para fazer o reconhecimento facial
"""
detector_face = dlib.get_frontal_face_detector()
detector_points = dlib.shape_predictor(shape_predictor)
facial_recognition = dlib.face_recognition_model_v1(model_face_recognition)
#Arquivos ja treinados
indices = np.load(indices_dir)
descriptors_facials = np.load(descriptors_dir)

"""
variavel responsavel por filtrar valores a baixo do ideal/precisao no reconhecimento
variavel respondavel por ajustar tamanho da imagem para que posso tornar maior
sendo assim detectar mais rostos
"""
limiar = 0.5
upsize = 1  

#tamanho da fonte do nome dado a pessoa pelo reconhecimento
size_fonte = 1
color_name = (0, 255, 255)
color_rectangle = (0, 255, 0)
font_text = cv.FONT_HERSHEY_COMPLEX_SMALL



def face_recognize(frame):
    faces_detected = detector_face(frame, upsize)
    num_faces = len(faces_detected)
    print(num_faces)

    if num_faces > 0:    
        for face in faces_detected:
            e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
            #obtem os pontos faciais do frame recebido e atribui a variavel
            facial_point = detector_points(frame, face)

            # transforma a imagem em um VETOR com as caracteristicas da face atraves do pontos faciais
            descriptor_facial = facial_recognition.compute_face_descriptor(frame, facial_point)

            # transforma em lista o vetor obtido das caracteristicas da face
            list_descriptor_facial = [fd for fd in descriptor_facial]

            # transforma em um array do tipo numpy atraves da lista
            np_array_descriptor_facial = np.asarray(list_descriptor_facial, dtype=np.float64)
            np_array_descriptor_facial = np_array_descriptor_facial[np.newaxis, :]

            #distancias obtidas no np_array
            distances = np.linalg.norm(np_array_descriptor_facial - descriptors_facials, axis=1)

            minimum = np.argmin(distances)

            #distancia minima
            distance_min = distances[minimum]

            if distance_min <= limiar:
                nome = os.path.split(indices[minimum])[1].split(".")[0]
            else:
                nome = "Desconhecido"

            cv.rectangle(frame, (e, t), (d, b), color_rectangle, 2)
            texto = "{} {:.4f}".format(nome, distance_min)
            cv.putText(frame, texto, (e, b+20), font_text, size_fonte, color_name)

    else: 
        retorno = False, None
        #return retorno
