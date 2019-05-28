import os
import cv2 as cv
import pickle as cPickle
import numpy as np
from facial_hog.FacialHog import FacialHog


det = FacialHog()

BASE_DIR = os.path.dirname(os.path.abspath("facial_hog"))
image_dir = os.path.join(BASE_DIR, "db-faces")
recursos_dir = os.path.join(BASE_DIR, "facial_hog/recursos")
descritor_file = os.path.join(recursos_dir, "descritores.npy")
indices_file = os.path.join(recursos_dir, "indices.pickle")

print("Base",BASE_DIR)
print(image_dir)
print(recursos_dir)
print(descritor_file)
print(indices_file)

indice = {}
descritores_faciais = None

def start_train():
    for root, dirs, files in os.walk(image_dir):
        print("Root",root)
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
                #print("Tamanho", len(imagem))
                indice, descritores_faciais = det.detecta_face(imagem, 1, label)

                print(path)
                #cv.imshow("Treinamento", imagem)
                #cv.waitKey(0) & 0xFF

    print("Tamanho: {} Formato: {}".format(len(descritores_faciais), descritores_faciais.shape))
    #print(descritores_faciais)
    print(indice)

    np.save(descritor_file, descritores_faciais)

    with open(indices_file, 'wb') as f:
        cPickle.dump(indice, f)

cv.destroyAllWindows()