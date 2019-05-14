import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

#parametro para a detecção de canto Shitomasi
feature_params = dict(maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize = 7)

#parametro para lucas kanade optica flow
lk_params = dict( winSize = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))

#cria alguma cor randomica
color = np.random.randint(0, 255, (100,3))

#Faz o primeiro frame e procura cornes no inteiro
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

#cria uma mascara na imagem para desenhar as proporções
mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #calcula optical flow
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    #seleciona o ponto bom
    good_new = p1[st==1]
    good_old = p0[st==1]

    #desenha
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c,d = old.ravel()
        mask = cv.line(mask, (a,b), (c,d), color[i].tolist(),2)
        frame = cv.circle(frame, (a,b), 5, color[i].tolist(), -1)
    img = cv.add(frame, mask)

    cv.imshow('Frame', img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

    #agora atualiza o proximo frame e proximo ponto
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)

cv.destroyAllWindows()
cap.release()

