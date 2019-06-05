from threading import Thread
import os
import time
import cv2 as cv

class Ocorrencia():

    BASE_DIR = os.path.dirname(__file__)
    DIR_OCORRENCIA = os.path.join(BASE_DIR, "ocorrencias")

    def __init__(self):
        self.person_picture = (None, None)

    def putOcorrencia(self, nome, frame):
        os.chdir(Ocorrencia.DIR_OCORRENCIA)
        date = self.getDate_now_dia_mes_ano()
        #print(date)
        #cria a pasta para salvar as ocorrencias do dia
        if not os.path.exists(date):
            print("[INFO]: Pasta do dia criada com sucesso")
            os.mkdir(date)
            
        self.person_picture = (nome, frame)

    def save_img(self):
        date = self.getDate_now_dia_mes_ano()
        os.chdir(date)
        #os.chdir(Ocorrencia.DIR_OCORRENCIA)
        time_ocorrencia = self.getDate_now_full()
        img = self.person_picture[1]
        img_item = self.person_picture[0]+time_ocorrencia+".png"
        cv.imwrite(img_item, img)
        os.chdir(Ocorrencia.DIR_OCORRENCIA)
        
    
    def getDate_now_dia_mes_ano(self):
        result_time = time.localtime()
        date = "{}-{}-{}".format(result_time.tm_mday,result_time.tm_mon ,result_time.tm_year)
        return date
    
    def getDate_now_full(self):
        result_time = time.localtime()
        date = "{}-{}-{}_{}:{}".format(result_time.tm_mday,result_time.tm_mon ,result_time.tm_year, result_time.tm_hour, result_time.tm_min)
        return date

    def clean_ocorrencia(self):
        self.person_picture = (None, None)
