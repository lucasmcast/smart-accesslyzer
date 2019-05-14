#importa os pacotes nescessarios
import datetime

class FPS:
    def __init__(self):
        #armazena a hora do inicio, a hora do termino, e o total do numero de frame
        #que foram examinados entre os intervalos inicial e final
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        #inicia o tempo
        self._start = datetime.datetime.now()
        return self

    def stop(self):
        #pega o tempo de parada
        self._end = datetime.datetime.now()

    def update(self):
        #incrementa o total do numero de frames examinado durante o começo e fim do intervalo
        self._numFrames +=1

    def elapsed(self):
        #returna o total de segundos entre o começo e o fim do intervalo
        return (self._end - self._start).total_seconds()

    def fps(self):
        return self._numFrames / self.elapsed()
