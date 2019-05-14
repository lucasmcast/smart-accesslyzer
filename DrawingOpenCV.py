import numpy as np
import cv2

#create a black image
img = np.zeros((512,512,3), np.uint8)

#draw a diagonal blue line with trickness of 5 px
img = cv2.line(img, (0,0), (511, 511), (255,0,0), 5)

img = cv2.rectangle(img, (384, 0), (510,128), (0,255,0),3)

cv2.imshow("Teste", img)
cv2.waitKey()
