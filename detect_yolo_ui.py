# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detect_yolo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 591, 531))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.image_txt = QtWidgets.QLabel(self.groupBox)
        self.image_txt.setGeometry(QtCore.QRect(10, 20, 571, 501))
        self.image_txt.setText("")
        self.image_txt.setObjectName("image_txt")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(610, 4, 211, 531))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.stop_bt = QtWidgets.QPushButton(self.groupBox_2)
        self.stop_bt.setGeometry(QtCore.QRect(110, 20, 75, 23))
        self.stop_bt.setObjectName("stop_bt")
        self.start_bt = QtWidgets.QPushButton(self.groupBox_2)
        self.start_bt.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.start_bt.setObjectName("start_bt")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(80, 80, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(150, 80, 47, 13))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.cam_txt = QtWidgets.QLineEdit(self.groupBox_2)
        self.cam_txt.setGeometry(QtCore.QRect(10, 110, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cam_txt.setFont(font)
        self.cam_txt.setObjectName("cam_txt")
        self.cachua_txt = QtWidgets.QLineEdit(self.groupBox_2)
        self.cachua_txt.setGeometry(QtCore.QRect(80, 110, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cachua_txt.setFont(font)
        self.cachua_txt.setObjectName("cachua_txt")
        self.chuoi_txt = QtWidgets.QLineEdit(self.groupBox_2)
        self.chuoi_txt.setGeometry(QtCore.QRect(150, 110, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chuoi_txt.setFont(font)
        self.chuoi_txt.setObjectName("chuoi_txt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stop_bt.setText(_translate("MainWindow", "Stop"))
        self.start_bt.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Cam"))
        self.label_2.setText(_translate("MainWindow", "Cà chua"))
        self.label_3.setText(_translate("MainWindow", "Chuối"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
