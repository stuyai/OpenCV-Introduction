import cv2
import os


path = os.path.join("data", "200427 (1080p).mp4" )
cap = cv2.VideoCapture(path)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  
fps = cap.get(cv2.CAP_PROP_FPS)
writer = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (int(width), int(height)))


count = 0;

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.imshow("Video", gray)
    writer.write(gray)
    count += 1
    print(f"Converting Frame: {count}", end = "\r")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break
    
print("Converting Frame: Done")
cap.release()
writer.release()
cv2.destroyAllWindows()