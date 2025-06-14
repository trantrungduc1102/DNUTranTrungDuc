import cv2
import numpy as np
from ultralytics import YOLO


model = YOLO("best.pt")  # Có thể thay bằng các phiên bản khác như yolo11s-cls.pt, yolo11m-cls.pt, v.v.

def open_camera():
    # Mở camera (0) là camera mặc định)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Không thể mở camera.")
        return

    while True:
        # Đọc từng khung hình từ camera
        ret, frame = cap.read()

        if not ret:
            print("Không thể nhận dạng khung hình.")
            break

        results = model(source=frame, conf=0.75)  # conf là ngưỡng độ tin cậy
        for result in results:
            if len(result.boxes.xyxy) > 0:
                for box, cls in zip(result.boxes.xyxy, result.boxes.cls):
                    x1, y1, x2, y2 = box
                    # Lấy tên lớp từ result.names
                    label = result.names[int(cls)]
                    print(label)
                    # Vẽ hình chữ nhật
                    color = (0, 255, 0)  # Màu xanh lá cây (BGR)
                    thickness = 2  # Độ dày của đường viền
                    # mean_np = np.mean(frame[])
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
                    # Vẽ tên lớp
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 0.6
                    font_thickness = 1
                    text_size = cv2.getTextSize(label, font, font_scale, font_thickness)[0]
                    text_x = int(x1)
                    text_y = int(y1) - 10 if int(y1) - 10 > 10 else int(
                        y1) + 10  # Đặt text phía trên box, tránh ra ngoài khung
                    cv2.putText(frame, label, (text_x, text_y), font, font_scale, color, font_thickness)

        # Hiển thị khung hình
        cv2.imshow('Camera', frame)

        # Nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Giải phóng tài nguyên
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    open_camera()