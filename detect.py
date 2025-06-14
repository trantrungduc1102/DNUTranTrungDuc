from ultralytics import YOLO
import cv2
import numpy as np

# 1. Tải mô hình YOLOv11 đã được huấn luyện sẵn cho tác vụ phân loại
# Sử dụng mô hình "yolo11n-cls.pt" (phiên bản nhỏ nhất) làm ví dụ
model = YOLO("best.pt")  # Có thể thay bằng các phiên bản khác như yolo11s-cls.pt, yolo11m-cls.pt, v.v.

# 2. Đọc hình ảnh cần phân loại
image_path = "Camera.png"  # Thay bằng đường dẫn đến hình ảnh của bạn
image = cv2.imread(image_path)

# 3. Thực hiện phân loại
results = model(source=image, conf=0.65, save_txt=False)  # conf là ngưỡng độ tin cậy

# 4. Xử lý và hiển thị kết quả
for result in results:
    print(result.boxes.xyxy[0])
    if len(result.boxes.xyxy) > 0:
        x1, y1, x2, y2 = result.boxes.xyxy[0]
        # Vẽ hình chữ nhật
        color = (0, 255, 0)  # Màu xanh lá cây (BGR)
        thickness = 2  # Độ dày của đường viền
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
    cv2.imshow('Rectangle', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()