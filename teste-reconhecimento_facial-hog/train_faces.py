import os
import cv2 as cv
import pickle as cPickle
import numpy as np
from PIL import Image
import dlib

detector_face = dlib.get_frontal_face_detector()
detector_pontos = dlib.shape_predictor("recursos/shape_predictor_68_face_landmarks.dat")
reconhecimento_facial = dlib.face_recognition_model_v1("recursos/dlib_face_recognition_resnet_model_v1.dat")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "imagens")

#print(image_dir)

current_id = 0
label_ids = {}
y_labels = []
x_train = []

indice = {}
idx = 0
descritores_faciais = None

for root, dirs, files in os.walk(image_dir):
    #print("Root",root)
    #print("dirs", dirs)
    #print("files", files)
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            #print(path)


            imagem = cv.imread(path)
            size = (550, 550)
            imagem = cv.resize(imagem, size)
            print("Tamanho", len(imagem))
            faces_detectadas = detector_face(imagem, 1)
            numero_faces_detectadas = len(faces_detectadas)
            print("numero de faces", numero_faces_detectadas)

            if numero_faces_detectadas > 1:
                print("Há mais de uma face na imagem {}".format(path))
                exit(0)
            elif numero_faces_detectadas < 1:
                print("Nenhuma face foi detectada {}".format(path))
                exit(0)

            for face in faces_detectadas:
                #obtem os postos facias detectado na imagem
                pontos_faciais = detector_pontos(imagem, face)

                #transforma a imagem em um VETOR com as caracteristicas da face atraves do pontos faciais
                descritor_facial = reconhecimento_facial.compute_face_descriptor(imagem, pontos_faciais)
                #print(format(path), type(descritor_facial))

                #transforma em lista o vetor obtido das caracteristicas da face
                lista_destritor_facial = [df for df in descritor_facial]
                #print("Lista de descritores", lista_destritor_facial, type(lista_destritor_facial))

                #transforma em um array do tipo numpy atraves da lista
                np_array_descritor_facial = np.asarray(lista_destritor_facial, dtype=np.float64)
                #print(np_array_descritor_facial, type(np_array_descritor_facial))

                np_array_descritor_facial = np_array_descritor_facial[np.newaxis, :]
                #print("Descritores",np_array_descritor_facial)

                if descritores_faciais is None:
                    descritores_faciais = np_array_descritor_facial
                else:
                    descritores_faciais = np.concatenate((descritores_faciais, np_array_descritor_facial), axis=0)

                indice[idx] = label #+ "." + str(num_foto)
                #print(indice[idx])
                idx += 1
                print(idx)

                """    
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1

                id_ = label_ids[label]

                print("labels_ids",label_ids[label])
                print(id_)
                """
            cv.imshow("Treinamento", imagem)
            cv.waitKey(0) & 0xFF

print("Tamanho: {} Formato: {}".format(len(descritores_faciais), descritores_faciais.shape))
print(descritores_faciais)
print(indice)

np.save("descritores.npy", descritores_faciais)

with open("indices.pickle", 'wb') as f:
    cPickle.dump(indice, f)

cv.destroyAllWindows()