import serial
from threading import Thread

class ArduinoRead:
    
    MAX_PORTAS = 3 # Número máximo de portas para verificação.

    def __init__(self):
        self.conexao = serial.Serial(self.getPortasEmUso(), 9600)
        self.status01 = ord(self.conexao.read()) 
        self.status02 = ord(self.conexao.read())
        self.dxaberta01 = ord(self.conexao.read()) 
        self.dxaberta02 = ord(self.conexao.read())
        

    def start(self):
        Thread(target=self._status, args=()).start()
        return self

    def _status(self):
        while True:
            self.status01 = ord(self.conexao.read())
            self.status02 = ord(self.conexao.read())
            self.dxaberta01 = ord(self.conexao.read())
            self.dxaberta02 = ord(self.conexao.read())
            
    def stop(self):
        self.conexao.close()

    def read_status(self):
        status = self.status01, self.status02, self.dxaberta01, self.dxaberta02
        return status

    
    def status_read(self):
        if self.status01 == 1:
            texto1 = "Porta 01 Aberta"
            color1 = (0,0,255)
            if self.dxaberta01 == 1:
                texto1 = "Porta 01 Deixada Aberta"
                color1 = (0,255,255)
        else:
            texto1 = "Porta 01 Fechada"
            color1 = (0,255,0)

        if self.status02 == 1:
            texto2 = "Porta 02 Aberta"
            color2 = (0,0,255)
            if self.dxaberta02 == 1:
                texto2 = "Porta 02 Deixada Aberta"
                color2 = (0,255,255)
        else:
            texto2 = "Porta 02 Fechada"
            color2 = (0,255,0)
        
        status = self.status01, self.dxaberta01, texto1, color1, self.status02, self.dxaberta02, texto2, color2
        return status

    def getPortasEmUso (self) :
        #Método para buscar as portas em uso
	    # Faz um loop de 1 ao número maximo de portas para verificação
		# e o concatena à string '/dev/ttyUSB':
        for p in range(ArduinoRead.MAX_PORTAS):
            porta = "/dev/ttyUSB{}".format(p)
            try:
                #tenta abrir a conexão
                s = serial.Serial(porta)
                # Tenta fechar a conexão
                s.close()
                return porta
            except (OSError, serial.SerialException):
                pass
