import os
import pickle
import numpy
from PIL import Image
import dlib

detector_face = dlib.get_frontal_face_detector()
detector_pontos = dlib.shape_predictor("recursos/shape_predictor_68_face_landmarks.dat")
reconhecimento_facial = dlib.face_recognition_model_v1("recursos/dlib_face_recognition_resnet_model_v1.dat")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "imagens")

print(image_dir)

for root, dirs, files in os.walk(image_dir):
    print("Root",root)
    print("dirs", dirs)
    print("files", files)