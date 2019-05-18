import dlib
import numpy as np

class FacialHog:
    
    def __init__(self):
        self.detector_face = dlib.get_frontal_face_detector()
        self.detector_pontos = dlib.shape_predictor("facial-hog/recursos/shape_predictor_68_face_landmarks.dat")
        self.reconhecimento_facial = dlib.face_recognition_model_v1("facial-hog/recursos/dlib_face_recognition_resnet_model_v1.dat")
        self.indice = {}
        self.idx = 0
        self.descritores_faciais = None


    def detecta_face(self, frame=None, parametro=1, label = None):


        if not frame is None:

            faces_detectadas = self.detector_face(frame, parametro)

            numero_faces_detectadas = len(faces_detectadas)

            if numero_faces_detectadas > 1:
                print("Há mais de uma face na imagem")
                exit(0)
            elif numero_faces_detectadas < 1:
                print("Nenhuma face foi detectada")
                exit(0)

            for face in faces_detectadas:

                np_array_descritor_facial = self.create_np_array_descriptor(frame, face)

                if self.descritores_faciais is None:
                    self.descritores_faciais = np_array_descritor_facial
                else:
                    self.descritores_faciais = np.concatenate((self.descritores_faciais, np_array_descritor_facial), axis=0)

                self.indice[self.idx] = label #+ "." + str(num_foto)
                #print(indice[idx])
                self.idx += 1
                print(self.idx)

            return (self.indice, self.descritores_faciais)
        else:
            print("imagem ou parametro não passado como parametro")
            return None

    #cria uma array numpy atraves do frame e da face recebida
    def create_np_array_descriptor(self, frame=None, face = None):

        # obtem os postos facias detectado na imagem
        pontos_faciais = self.detector_pontos(frame, face)

        # transforma a imagem em um VETOR com as caracteristicas da face atraves do pontos faciais
        descritor_facial = self.reconhecimento_facial.compute_face_descriptor(frame, pontos_faciais)
        # print(format(path), type(descritor_facial))

        # transforma em lista o vetor obtido das caracteristicas da face
        lista_destritor_facial = [df for df in descritor_facial]
        # print("Lista de descritores", lista_destritor_facial, type(lista_destritor_facial))

        # transforma em um array do tipo numpy atraves da lista
        np_array_descritor_facial = np.asarray(lista_destritor_facial, dtype=np.float64)
        # print(np_array_descritor_facial, type(np_array_descritor_facial))

        np_array_descritor_facial = np_array_descritor_facial[np.newaxis, :]
        # print("Descritores",np_array_descritor_facial)

        return np_array_descritor_facial
