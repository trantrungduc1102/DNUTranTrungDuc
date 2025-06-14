import cv2


def list_available_cameras(max_cameras=10):
    available_cameras = []

    for i in range(max_cameras):
        cap = cv2.VideoCapture(i)

        if cap.isOpened():
            available_cameras.append(i)
            cap.release()  # Giải phóng camera nếu mở thành công

    return available_cameras


if __name__ == '__main__':
    cameras = list_available_cameras()

    if cameras:
        print("Các camera khả dụng:")
        for cam_index in cameras:
            print(f"Camera index: {cam_index}")
    else:
        print("Không tìm thấy camera nào.")