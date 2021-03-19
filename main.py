import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from GlassBg import SetGlassBg

from ui import SimpleWinlockerUI



class SimpleWinlocker(SimpleWinlockerUI):
    def __init__(self, screen_size):
    	super(SimpleWinlocker, self).__init__(screen_size)
    	#self.ui = SimpleWinlockerUI(screen_size)

    	self.init_UI()

    def init_UI(self):
    	self.unlock_btn.clicked.connect(self.unlock_window)

    def unlock_window(self):
    	self.label.setText(("Windows unlocked"))
    	self.label.adjustSize()
    	QTimer.singleShot(750, self.close) #close window
    	print('test')



app = QApplication(sys.argv)

win = SimpleWinlocker(app.desktop().screenGeometry())
#win = SimpleWinlockerUI(app.desktop().screenGeometry())
SetGlassBg(win)
win.showFullScreen()
sys.exit(app.exec_())
