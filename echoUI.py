# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisUI(object):
    def setupUi(self, echoUI):
        echoUI.setObjectName("jarvisUI")
        echoUI.resize(970, 681)
        self.centralwidget = QtWidgets.QWidget(echoUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 971, 681))
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        pixmap = QtGui.QPixmap("C:/Users/shrey/Desktop/jarvisGUI/wallpaper/7gRx.gif")
        print("Loaded:", not pixmap.isNull())
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.label.lower()



        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 620, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 620, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"background-color: rgb(255, 85, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        echoUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(echoUI)
        QtCore.QMetaObject.connectSlotsByName(echoUI)

    def retranslateUi(self, echoUI):
        _translate = QtCore.QCoreApplication.translate
        echoUI.setWindowTitle(_translate("echoUI", "MainWindow"))
        self.pushButton.setText(_translate("echoUI", "RUN"))
        self.pushButton_2.setText(_translate("echoUI", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    echoUI = QtWidgets.QMainWindow()
    ui = Ui_jarvisUI()
    ui.setupUi(echoUI)
    echoUI.show()
    sys.exit(app.exec_())
