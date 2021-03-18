from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from GlassBg import SetGlassBg

import sys



class SimpleWinlockerUI(QMainWindow):
    def __init__(self, screen_size):
        super(SimpleWinlockerUI, self).__init__()
        self.pointsize = 64
        self.screen_size = screen_size
        print(self.screen_size)
        self.initUI()


    def initUI(self):
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(self.pointsize)

        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumWidth(1024)
        self.label.setMinimumHeight(128)
        self.label.setStyleSheet("color: rgba(11, 11, 11, 125);")
        self.label.move(self.screen_size.width() / 2 - self.label.width() / 2, self.screen_size.height() - self.label.height() / 2 - self.pointsize)
        self.label.setFont(font)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setMinimumWidth(1024)
        self.lineEdit.setMinimumHeight(256)
        self.lineEdit.move(self.screen_size.width() / 2 - self.lineEdit.width() / 2, self.screen_size.height() / 2 - self.lineEdit.height() / 2)
        self.lineEdit.setStyleSheet("background-color: transparent;\n"
        "color: rgba(11, 11, 11, 125);\n"
        "\n"
        "selection-color: rgb(255, 255, 255, 2);\n"
        "selection-background-color: rgba(91, 91, 91, .3);\n"
        "\n"
        "border: 8px rgba(11, 11, 11, 125);\n"
        "border-radius: 16px;"
        "\n"
        "text-align: center;")
        self.lineEdit.setFont(font)

        self.unlock_btn = QtWidgets.QPushButton(self)
        self.unlock_btn.setMinimumWidth(512)
        self.unlock_btn.setMinimumHeight(128)
        self.unlock_btn.move(self.screen_size.width() / 2 - self.unlock_btn.width() / 2, self.screen_size.height() - self.unlock_btn.height() / 2 - 64 - (self.screen_size.height() - self.label.height() / 2 - 64) / 4)
        self.unlock_btn.setFont(font)
        self.unlock_btn.setStyleSheet("color: rgba(11, 11, 11, 125); background-color: rgba(0, 0, 0, .04); border-radius: 32px;")
        self.unlock_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.retranslateUi()

        # label.setMinimumWidth(1024)
        # label.setMinimumHeight(128)
    def update(self):
        self.label.adjustSize()

    def retranslateUi(self):
    	_translate = QtCore.QCoreApplication.translate

    	self.setWindowTitle('Simple winlocker')
    	self.unlock_btn.setText("Unlock")
    	self.label.setText("Windows locked")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    

    win = SimpleWinlockerUI(app.desktop().screenGeometry())
    SetGlassBg(win)

    win.showFullScreen()
    sys.exit(app.exec_())