import cv2
import numpy as np
import os

path = os.path.join("data", "200427 (1080p).mp4" )
cap = cv2.VideoCapture(path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break

cap.release()
cv2.destroyAllWindows()


