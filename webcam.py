import cv2
import numpy as np
import os

print(cv2.__file__)
camera = cv2.VideoCapture("rtsp://usuario:senha@dominio/ip:554/h264/ch5/main/av_stream")
#rtsp://usuario:senha@dominio/ip:554/h264/ch1/main/av_stream
#"http://138.118.33.201:80/mjpg/video.mjpg"
#Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter("output1.avi", fourcc, 20.0,(640,480))



#if os.path.isfile("output.avi"):
#    os.remove("output.avi")

while (camera.isOpened()):
    # Capture frame-by-frame
    ret, frame = camera.read()

    if ret == True:
        # Handles the mirroring of the current frame
        #frame = cv2.flip(frame, 2)

        #write the flipped frame
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)

    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
camera.release()
out.release()
cv2.destroyAllWindows()
