import cv2 as cv
import sys
import pytesseract
 
cap = cv.VideoCapture(0)

config = ('-l eng --oem 1 --psm 7')

while True:

    ret, frame = cap.read()
     
    # Uncomment the line below to provide path to tesseract manually
    # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    # Define config parameters.
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    
 
 
    # Run tesseract OCR on image
    text = pytesseract.image_to_string(frame, config=config)
    # Print recognized text
    print(text)
    cv.imshow("Frame", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
cap.release()