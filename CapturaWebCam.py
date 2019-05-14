import sys
import cv2
import signal

end = False

#-----------------------------------------
def signal_handler(signal, frame):
    global end
    end = True
#-----------------------------------------
cap = cv2.VideoCapture(0)

# tenta abrir a webcam, e falha caso nao conseguir
if not cap.isOpened():
    print("Nao foi possivel abrir a webcam")
    sys.exit(-1)

#cria o arquivo de video de saida
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
out = cv2.VideoWriter("record.avi", fourcc, 20.0, (640,480))

#captura o sinal de CTRL+C no terminal
signal.signal(signal.SIGINT, signal_handler)
print("Capturando o video da webcam -- pressione CTRL+C para encerar")

#processa enquanto o usuario nao encerrar
while(not end):
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        print("oops, A captura falhou")
        break

print("Captura encerrada")

#--encerra tudo
cap.release()
out.release()