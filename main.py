# main.py

import cv2 as cv
import torch
from ultralytics import YOLO
from buzzer import PassiveBuzzer

# Load model YOLO
model = YOLO('yolov8n.pt')

if torch.cuda.is_available():
    model.to('cuda')
    print("🔥 Model running on GPU")
else:
    print("⚠️ No GPU, using CPU")

# Khởi tạo buzzer (passive), không có pin GPIO nên giả lập
buzzer = PassiveBuzzer()

# Mở webcam
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
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

        name = model.names[cls]

        # Buzzer logic
        if name == 'person':
            buzzer.play_note('B')  # Si
        elif name in ['cat', 'dog', 'horse', 'sheep', 'cow']:  # animal class
            buzzer.play_note('A')  # La

    cv.imshow('YOLOv8 + Passive Buzzer', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
