from thread.VideoStream import VideoStream

from thread import VideoStream
import cv2
import time

#video_stream = VideoStream("rtsp://usuario:senha@192.168.2.50:1025/Streaming/Channels/101/").start()
#video_stream1 = VideoStream("rtsp://usuario:senha@10.35.27.9:554/h264/ch1/main/av_stream").start()
video_stream = VideoStream(0).start()
#video_show = VideoShow(video_stream.frame).start()
while True:

    if (cv2.waitKey(1) == ord('q') or video_stream.stopped):
        video_stream.stop()
        break

    frame = video_stream.read()
    #frame1 = video_stream1.read()
    print(len(frame))
    cv2.imshow("video", frame)
    #cv2.imshow("video1", frame1)

cv2.destroyAllWindows()
