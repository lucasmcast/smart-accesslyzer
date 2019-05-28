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

class FacialRecognition():

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

        self.limiar = 0.5
        self.upsize = 1

        self.size_fonte = 1
        self.color_name = (0, 255, 255)
        self.color_rectangle = (0, 255, 0)
        self.font_text = cv.FONT_HERSHEY_COMPLEX_SMALL

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
    
                retorno =  True, nome
                return retorno
        else: 
            retorno = False, None
            return retorno
    

