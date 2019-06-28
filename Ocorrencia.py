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
        #os.chdir(Ocorrencia.DIR_OCORRENCIA)
        print(os.getcwd())
        data = self.getDate_now_dia_mes_ano()
        dir_save = os.path.join(Ocorrencia.DIR_OCORRENCIA, data)
        print(dir_save)
        #cria a pasta para salvar as ocorrencias do dia
        if not os.path.exists(dir_save):
            print("[INFO]: Pasta do dia criada com sucesso")
            os.mkdir(dir_save)
            
        self.person_picture = (nome, frame)
        #os.chdir(Ocorrencia.BASE_DIR)

    def save_img(self):
        os.chdir(Ocorrencia.DIR_OCORRENCIA)
        data = self.getDate_now_dia_mes_ano()
        if not os.path.exists(data):
            os.mkdir(data)
        os.chdir(data)
        #os.chdir(Ocorrencia.DIR_OCORRENCIA)
        time_ocorrencia = self.getDate_now_full()
        img = self.person_picture[1]
        img_item = self.person_picture[0]+time_ocorrencia+".png"
        cv.imwrite(img_item, cv.cvtColor(img, cv.COLOR_RGB2BGR))
        os.chdir(Ocorrencia.BASE_DIR)


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

