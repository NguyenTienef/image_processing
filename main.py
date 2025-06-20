import cv2 as cv
import torch
import os
import time
from ultralytics import YOLO
import matplotlib.pyplot as plt


model = YOLO('C:/Users/Admin/OneDrive/Máy tính/buzzer_AI/YOLOv8/yolov8x.pt')

if torch.cuda.is_available():
    model.to('cuda')
    print("🔥 Model đang chạy trên GPU")
else:
    print("⚠️ Không có GPU, model chạy trên CPU")


cap = cv.VideoCapture(0)
buzzer_timeline = []

def beep():
    os.system("echo /a") 

start_time = time.time()
while True:
    ret, frame = cap.read()
    frame = cv.flip(frame, 1) 
    frame = cv.resize(frame, (640, 480))  

    if not ret:
        break

    results = model(frame, imgsz=320, conf=0.5)[0]

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])
        cls = int(box.cls[0])
        label = f'{model.names[cls]} {conf:.2f}'
        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv.putText(frame, label, (x1, y1 - 10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        
        if model.names[cls] == 'person':
            beep()
            buzzer_timeline.append(time.time() - start_time)

    cv.imshow('YOLOv8 with Buzzer Sim', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


plt.figure(figsize=(10, 3))
plt.eventplot(buzzer_timeline, orientation='horizontal', colors='r')
plt.title("Buzzer Activated Timeline")
plt.xlabel("Time (s)")
plt.yticks([])
plt.show()
