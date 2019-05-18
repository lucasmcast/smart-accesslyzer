import os
import glob #percorrer os arquivos de imagens
import pickle as cPickle #grvação dos arquivos de treinamento
import dlib
import cv2
import numpy as np
import time

detector_face = dlib.get_frontal_face_detector()
detector_pontos = dlib.shape_predictor("recursos/shape_predictor_68_face_landmarks.dat")
reconhecimento_facial = dlib.face_recognition_model_v1("recursos/dlib_face_recognition_resnet_model_v1.dat")

indice = {}
idx = 0
descritores_faciais = None

#percorre arquivo por arquivo com o laço for
for arquivo in glob.glob(os.path.join("fotos/treinamento", "*.jpg")):
    print(arquivo)
    imagem = cv2.imread(arquivo)
    faces_detectadas = detector_face(imagem, 1)
    numero_faces_detectadas = len(faces_detectadas)

    if numero_faces_detectadas > 1:
        print("Há mais de uma face na imagem {}".format(arquivo))
        exit(0)
    elif numero_faces_detectadas < 1:
        print("Nenhuma face foi detectada {}".format(arquivo))
        exit(0)

    for face in faces_detectadas:
        pontos_faciais = detector_pontos(imagem, face)
        descritor_facial = reconhecimento_facial.compute_face_descriptor(imagem, pontos_faciais)
        print(format(arquivo))

        lista_destritor_facial = [df for df in descritor_facial]
        #print(lista_destritor_facial)

        np_array_descritor_facial = np.asarray(lista_destritor_facial, dtype=np.float64)
        #print(np_array_descritor_facial)

        np_array_descritor_facial = np_array_descritor_facial[np.newaxis, :]
        #print(np_array_descritor_facial)

        if descritores_faciais is None:
            descritores_faciais = np_array_descritor_facial
        else:
            descritores_faciais = np.concatenate((descritores_faciais, np_array_descritor_facial), axis=0)

        indice[idx] = arquivo
        idx +=1

    #print(numero_faces_detectadas)
    #cv2.imshow("Treinamento", imagem)
    #cv2.waitKey(0) & 0xFF
#print("Tamanho: {} Formato: {}".format(len(descritores_faciais), descritores_faciais.shape))
print(descritores_faciais)
print("Indices",indice)

np.save("descritores_rn.npy", descritores_faciais)
with open("indices_rn.pickle", 'wb') as f:
    cPickle.dump(indice, f)

cv2.destroyAllWindows()