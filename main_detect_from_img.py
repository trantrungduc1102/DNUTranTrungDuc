import datetime
import sys
import threading

import cv2
import numpy as np
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidgetItem
from ultralytics import YOLO

from giaodien_yolo_ui import Ui_MainWindow



class MainGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setupUi(self)
        self.chon_duong_dan_bt.clicked.connect(self.openFileDialog)
        self.chon_duong_dan_bt_2.clicked.connect(self.detect_yolo)
        self.label_2.setFixedSize(120, 25)

        self.model = YOLO("best.pt")  # Có thể thay bằng các phiên bản khác như yolo11s-cls.pt, yolo11m-cls.pt, v.v.
    def detect_yolo(self):
        try:
            # 2. Đọc hình ảnh cần phân loại
            image_path = self.browser_path_txt.text()  # Thay bằng đường dẫn đến hình ảnh của bạn
            image = cv2.imread(image_path)

            # 3. Thực hiện phân loại
            results = self.model(source=image, conf=0.65, save_txt=False)  # conf là ngưỡng độ tin cậy
            for result in results:
                if len(result.boxes.xyxy) > 0:
                    x1, y1, x2, y2 = result.boxes.xyxy[0]
                    # Vẽ hình chữ nhật
                    color = (0, 255, 0)  # Màu xanh lá cây (BGR)
                    thickness = 2  # Độ dày của đường viền
                    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, thickness)
                    class_names = ['cachua', 'cam', 'chuoi']
                    class_id = int(result.boxes.cls[0])  # Lấy chỉ số lớp
                    class_name = class_names[class_id]  # Lấy tên quả từ danh sách
                    self.label_2.setText('Result: ' + class_name)
            self.label.clear()
            # Chuyển đổi màu BGR sang RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Chuyển đổi hình ảnh thành QPixmap
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            qImg = QPixmap.fromImage(QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888))

            self.label.setPixmap(qImg.scaled(self.label.size(), aspectRatioMode=1))  # Tỉ lệ ảnh

        except Exception as ex:
            print(ex)

    def openFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Chọn ảnh", "", "Images (*.png *.xpm *.jpg *.jpeg);;All Files (*)", options=options)
        if fileName:
            self.browser_path_txt.setText(fileName)  # Lưu đường dẫn vào QLineEdit
            self.displayImage(fileName)  # Hiển thị ảnh

    def displayImage(self, filePath):
        pixmap = QPixmap(filePath)
        self.label.setPixmap(pixmap.scaled(self.label.size(), aspectRatioMode=1))  # Tỉ lệ

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainGUI()
    main_window.show()
    sys.exit(app.exec_())