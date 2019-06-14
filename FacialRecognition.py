"""
    Autor: Lucas Martins de Castro
    Data: 21/05/2019
    Descricao: classe responsavel por fazer o reconhecimento facial comparando
    as imagens do banco de dados ja treinadas.
"""

import cv2 as cv
import dlib
import numpy as np
import os
from threading import Thread

class FacialRecognition():

    FONT_TEXT = cv.FONT_HERSHEY_COMPLEX_SMALL
    SIZE_TEXT = 0.8
    COLOR_TEXT = (0, 255, 255)
    COLOR_RECTANGLE = (0, 255, 0)
    SIZE_LINE_RECT = 1
    
    LIMIAR = 0.5
    

    def __init__(self):
        self.shape_predictor = "facial_hog/recursos/shape_predictor_68_face_landmarks.dat"
        self.model_face_recognition = "facial_hog/recursos/dlib_face_recognition_resnet_model_v1.dat"
        self.indices_dir = "facial_hog/recursos/indices.pickle"
        self.descriptors_dir = "facial_hog/recursos/descritores.npy"

        self.detector_face = dlib.get_frontal_face_detector()
        self.detector_points = dlib.shape_predictor(self.shape_predictor)
        self.facial_recognition = dlib.face_recognition_model_v1(self.model_face_recognition)
        #Arquivos ja treinados
        self.indices = np.load(self.indices_dir)
        self.descriptors_facials = np.load(self.descriptors_dir)

        self.upsize = 1 

        self.detectou = False
        self.nome = ''
        self.count = 0

        self.draw_object = (0,0,0,0,'')

    def face_recognize(self, frame):
        if self.count % 2 == 0:
            faces_detected = self.detector_face(frame, self.upsize)
            num_faces = len(faces_detected)
            #print(num_faces)
            if num_faces > 0:    
                for face in faces_detected:
                    e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
                    #print(e, t, d, b)
                    #obtem os pontos faciais do frame recebido e atribui a variavel
                    facial_point = self.detector_points(frame, face)
                    # transforma a imagem em um VETOR com as caracteristicas da face atraves do pontos faciais
                    descriptor_facial = self.facial_recognition.compute_face_descriptor(frame, facial_point)
                    # transforma em lista o vetor obtido das caracteristicas da face
                    list_descriptor_facial = [fd for fd in descriptor_facial]
                    # transforma em um array do tipo numpy atraves da lista
                    np_array_descriptor_facial = np.asarray(list_descriptor_facial, dtype=np.float64)
                    np_array_descriptor_facial = np_array_descriptor_facial[np.newaxis, :]
                    #distancias obtidas no np_array
                    distances = np.linalg.norm(np_array_descriptor_facial - self.descriptors_facials, axis=1)
                    minimum = np.argmin(distances)
                    #distancia minima
                    distance_min = distances[minimum]
                    if distance_min <= FacialRecognition.LIMIAR:
                        nome = os.path.split(self.indices[minimum])[1].split(".")[0]
                    else:
                        nome = "Desconhecido"
                    #cv.rectangle(frame, (e, t), (d, b), self.color_rectangle, 2)
                    texto = "{} {:.4f}".format(nome, distance_min)
                    self.draw_object = e, t, d, b, texto
                    #self.draw_rectangle_text(frame, face, 2, texto)
                    #cv.putText(frame, texto, (e, b+20), self.font_text, self.size_fonte, self.color_name)
                    self.detectou = True
                    self.nome = nome
            else: 
                self.detectou = False
                self.nome = ''
        self.count += 1

    def draw_rectangle_text(self, frame, face, thinckness=1, texto=''):
        e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))

        cv.rectangle(frame, (e, t), (d, b), FacialRecognition.COLOR_RECTANGLE, thinckness)
        cv.putText(frame, texto, (e, b+20), FacialRecognition.FONT_TEXT, FacialRecognition.SIZE_TEXT, FacialRecognition.COLOR_TEXT)
    

    

