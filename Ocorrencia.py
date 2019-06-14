from threading import Thread
import os
from datetime import date, datetime
import cv2 as cv
import numpy as np

class Ocorrencia():

    BASE_DIR = os.path.dirname(__file__)
    DIR_OCORRENCIA = os.path.join(BASE_DIR, "ocorrencias")
    DEFAULT_SIZE = (200,200)
    DEFAULT_IMG = np.zeros(DEFAULT_SIZE, dtype=np.uint8)

    def __init__(self):
        self.person_picture = ("Ninguem Detectado", Ocorrencia.DEFAULT_IMG)

    def putOcorrencia(self, nome, frame):
        os.chdir(Ocorrencia.DIR_OCORRENCIA)
        data = self.getDate_now_dia_mes_ano()
        #print(date)
        #cria a pasta para salvar as ocorrencias do dia
        if not os.path.exists(data):
            print("[INFO]: Pasta do dia criada com sucesso")
            os.mkdir(data)
            
        self.person_picture = (nome, frame)

    def save_img(self):
        os.chdir(Ocorrencia.DIR_OCORRENCIA)
        data = self.getDate_now_dia_mes_ano()
        os.chdir(data)
        #os.chdir(Ocorrencia.DIR_OCORRENCIA)
        time_ocorrencia = self.getDate_now_full()
        img = self.person_picture[1]
        img_item = self.person_picture[0]+time_ocorrencia+".png"
        cv.imwrite(img_item, img)
        os.chdir(Ocorrencia.DIR_OCORRENCIA)
        
    
    def getDate_now_dia_mes_ano(self):
        result_time = date.today()
        data = result_time.strftime("%d-%m-%Y")
        return data
    
    def getDate_now_full(self):
        result_time = datetime.now()
        data = result_time.strftime("%d-%m-%Y %H:%M")
        return data

    def clean_ocorrencia(self):
        self.person_picture = ("Ninguem Detectado", Ocorrencia.DEFAULT_IMG)
