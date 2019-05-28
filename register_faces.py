import cv2 as cv
import os
import os.path
import dlib
import shutil
from thread import VideoStream
from facial_hog.train_faces import start_train

count_foto = 1
#vai para o diretorio especificado
os.chdir('db-faces')

nome = input("Digite seu nome para cadastro da imagem:\n")
print("Criando um diretorio com o nome {}".format(nome))
if not os.path.exists(nome):
    os.mkdir(nome)
    os.chdir(nome)

    print("Diretorio Criado com Sucesso!!")
    cap = VideoStream("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/sub/av_stream").start()
    while True:
        frame = cap.read()

        cv.imshow("Cadastro", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            img_file = "0"+str(count_foto)+".png"
            cv.imwrite(img_file, frame)
            break
    cap.stop()
    cv.destroyAllWindows()
else:
    os.chdir(nome)
    #print(os.getcwd())
    path = "01.png"
    print(path)
    img = cv.imread(path)
    cv.imshow("Pessoa", img)
    k = cv.waitKey(0)
    if (k == ord('s')):
        cap = VideoStream("rtsp://tcc2:tcc28080@192.168.2.50:1025/h264/ch1/sub/av_stream").start()
        while True:
            frame = cap.read()

            cv.imshow("Cadastro", frame)
            if (cv.waitKey(1) & 0xFF == ord('s')):

                print(os.getcwd())
                qtd_files = len(os.listdir("."))
                if qtd_files < 9:
                    img_file = "0"+str(qtd_files+1)+".png"
                    cv.imwrite(img_file, frame)
                else:
                    img_file = str(qtd_files+1)+".png"
                    cv.imwrite(img_file,frame)
                break
cap.stop()
cv.destroyAllWindows()
        
start_train()      




