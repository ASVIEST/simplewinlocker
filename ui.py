from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from GlassBg import SetGlassBg

import sys


def window():
	app = QApplication(sys.argv)
	win = QMainWindow()
	SetGlassBg(win)
	screen_size = app.desktop().screenGeometry()

	label = QtWidgets.QLabel(win)
	label.setText("Windows locked")
	label.setMinimumWidth(1024)
	label.setMinimumHeight(128)

	font = QtGui.QFont()
	font.setFamily("Verdana")
	pointsize = 64
	font.setPointSize(pointsize)
	label.setFont(font)

	labelcenter = (screen_size.width() / 2 - label.width() / 2, screen_size.height() / 2 - label.height() / 2) #center of label
	labelcenterdown = (screen_size.width() / 2 - label.width() / 2, screen_size.height() - label.height() / 2 - pointsize)
	label.setStyleSheet("color: rgba(11, 11, 11, 125);")
	label.move(*labelcenterdown)


	lineEdit = QtWidgets.QLineEdit(win)
	lineEdit.setMinimumWidth(1024)
	lineEdit.setMinimumHeight(128)
	lineEdit.move(screen_size.width() / 2 - lineEdit.width() / 2, screen_size.height() / 2 - lineEdit.height() / 2)

	
	lineEdit.setStyleSheet("background-color: transparent;\n"
	"color: rgba(11, 11, 11, 125);\n"
	"\n"
	"selection-color: rgb(255, 255, 255, 2);\n"
	"selection-background-color: rgba(91, 91, 91, .3);\n"
	"\n"
	"border: 8px rgba(11, 11, 11, 125);\n"
	"border-radius: 16px;"
	"\n"
	"text-align: center;")

	lineEdit.setFont(font)



	unlock_btn = QtWidgets.QPushButton(win)
	unlock_btn.setMinimumWidth(512)
	unlock_btn.setMinimumHeight(128)
	unlock_btn.move(screen_size.width() / 2 - unlock_btn.width() / 2, screen_size.height() - unlock_btn.height() / 2 - 64 - (screen_size.height() - label.height() / 2 - 64) / 4)
	unlock_btn.setText("Unlock")
	unlock_btn.setFont(font)
	unlock_btn.setStyleSheet("color: rgba(11, 11, 11, 125); background-color: rgba(0, 0, 0, .04); border-radius: 32px;")




	win.showFullScreen()
	sys.exit(app.exec_())

window()