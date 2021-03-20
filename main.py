import sys
import ctypes

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from GlassBg import SetGlassBg

from ui import SimpleWinlockerUI


from DisableHotkeys import DisableHotkeys
from HideTaskbar import unhide_taskbar, hide_taskbar

class SimpleWinlocker(SimpleWinlockerUI):
    def __init__(self, screen_size):
    	super(SimpleWinlocker, self).__init__(screen_size)
    	self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    	self.lock_window()
    	self.password = '1234'
    	#self.ui = SimpleWinlockerUI(screen_size)

    	self.init_UI()

    def init_UI(self):
    	self.unlock_btn.clicked.connect(self.chek_password)

    def chek_password(self):
    	print(self.lineEdit.text())
    	if self.lineEdit.text() == self.password:
    		self.unlock_window()

    def unlock_window(self):
    	self.label.setText("Windows unlocked")
    	self.label.adjustSize()
    	QTimer.singleShot(300, self.close) #close window
    	unhide_taskbar()
    	print('test')

    def lock_window(self):
    	pass
    	#disabling hotkeys
    	#hide_taskbar()

    def update(self, e):
    	print('test')



app = QApplication(sys.argv)
DisableHotkeys()
	
win = SimpleWinlocker(app.desktop().screenGeometry())
#win = SimpleWinlockerUI(app.desktop().screenGeometry())
SetGlassBg(win)
win.showFullScreen()
sys.exit(app.exec_())
