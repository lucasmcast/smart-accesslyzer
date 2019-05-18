import os
import glob #percorrer os arquivos de imagens
import _pickle as cPickle #grvação dos arquivos de treinamento
import dlib
import cv2
import numpy as np

detector_face = dlib.get_frontal_face_detector()
detector_pontos = dlib.shape_predictor("recursos/shape_predictor_68_face_landmarks.dat")
reconhecimento_facial = dlib.face_recognition_model_v1("recursos/dlib_face_recognition_resnet_model_v1.dat")

indices = np.load("treinamento_teste/indices_rn.pickle")
descritores_faciais = np.load("treinamento_teste/descritores_rn.npy")

#variavel responsavel por filtrar valores a baixo do ideal/precisão no reconhecimento
limiar = 0.5

#percorre arquivo por arquivo com o laço for
for arquivo in glob.glob(os.path.join("fotos", "*.jpg")):

    imagem = cv2.imread(arquivo)
    faces_detectadas = detector_face(imagem, 2)

    for face in faces_detectadas:
        e, t, d, b = (int(face.left()), int(face.top()), int(face.right()), int(face.bottom()))
        pontos_faciais =  detector_pontos(imagem, face)
        descritor_facial = reconhecimento_facial.compute_face_descriptor(imagem, pontos_faciais)
        lista_descritor_facial = [fd for fd in descritor_facial]

        np_array_descritor_facial = np.asarray(lista_descritor_facial, dtype=np.float64)
        np_array_descritor_facial = np_array_descritor_facial[ np.newaxis, :]

        distancias = np.linalg.norm(np_array_descritor_facial - descritores_faciais, axis=1)
        print("Distancia: {}".format(distancias))
        #pega o indice do menor valor do array
        minimo = np.argmin(distancias)
        print(minimo)
        #pega o valor do indice com a menor distancia(valor)
        distancia_minima = distancias[minimo]
        print(distancia_minima)

        if distancia_minima <= limiar:
            nome = os.path.split(indices[minimo])[1].split(".")[0]
        else:
            nome = " "


        cv2.rectangle(imagem, (e,t), (d,b), (0,255,255), 2)
        texto = "{} {:.4f}".format(nome, distancia_minima)
        cv2.putText(imagem, texto, (d,t), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (0,255,255))

    cv2.imshow("Detector HOG", imagem)
    cv2.waitKey(0)

cv2.destroyAllWindows()