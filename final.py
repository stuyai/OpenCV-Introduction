import cv2
import os
import numpy as np


NAME = "AWESOME VID"
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

pt1, pt2 = (0, 0), (0, 0)
top_left_clicked, bottom_right_clicked = False, False


def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, top_left_clicked, bottom_right_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        if top_left_clicked and bottom_right_clicked:
            pt1, pt2 = (0, 0), (0, 0)
            top_left_clicked, bottom_right_clicked = False, False

        elif not top_left_clicked:
            pt1 = (x, y)
            top_left_clicked = True

        elif not bottom_right_clicked:
            pt2 = (x, y)
            bottom_right_clicked = True


cv2.namedWindow(NAME)
cv2.setMouseCallback(NAME, draw_rectangle)


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    if top_left_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(255, 0, 255), thickness=-1)

    if top_left_clicked and bottom_right_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 2)

    cv2.imshow(NAME, frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cap.release()
        break

cap.release()
cv2.destroyAllWindows()
