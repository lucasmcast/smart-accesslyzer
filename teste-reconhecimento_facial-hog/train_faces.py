import os
import cv2 as cv
import pickle as cPickle
import numpy as np


det = FacialHog()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "imagens")

#print(image_dir)

indice = {}
descritores_faciais = None

def start_train():
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
                indice, descritores_faciais = det.detecta_face(imagem, 1, label)

                cv.imshow("Treinamento", imagem)
                cv.waitKey(0) & 0xFF

    print("Tamanho: {} Formato: {}".format(len(descritores_faciais), descritores_faciais.shape))
    print(descritores_faciais)
    print(indice)

    np.save("recursos/descritores.npy", descritores_faciais)

    with open("recursos/indices.pickle", 'wb') as f:
        cPickle.dump(indice, f)

#executa a função para treinar o algoritmo
start_train()

cv.destroyAllWindows()