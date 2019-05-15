import os
import cv2 as cv
import numpy as np
from PIL import Image
import pickle
import dlib

#face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
#recognizer = cv.face.LBPHFaceRecognizer_create()

detector_face = dlib.get_frontal_face_detector()
detector_pontos = dlib.shape_predictor("recursos/shape_predictor_68_face_landmarks.dat")
reconhecimento_facial = dlib.face_recognition_model_v1("recursos/dlib_face_recognition_resnet_model_v1.dat")

BASE_DIR = os.path.dirname(o.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "imagens")

print(image_dir)
print(BASE_DIR)

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()
            print(label, path)
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1

            id_ = label_ids[label]

            print(label_ids)
            print(id_)
            #y_labels.append(label) #some number
            #x_train.append(path) # verify this image, turn into a NUMPY array, gray
            pil_image =  Image.open(path).convert("L") #grayscale
            size = (550, 550)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image, "uint8")
            print(pil_image)
            print(image_array)

            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)

print(x_train)
print(y_labels)

with open("labels.pickle", "wb") as f:
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.xml")