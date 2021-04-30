import sys
import os
import time	
from ui_untitled import *
from PySide2 import QtCore
progress_val =0

i = 0 
class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#self.show()
		self.ui.pushButton.clicked.connect(self.go)
		self.ui.pushButton1.clicked.connect(self.change)
		QtCore.QTimer.singleShot(0,lambda:self.ui.widget.rpb_setValue(0))
		self.change()
	def go(self):
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(60)
		

	def update(self):
		global progress_val
		self.ui.widget.rpb_setValue(progress_val)
		if progress_val>420:
			progress_val = 0
		progress_val+=1

	def change(self):
		dic = {0:'Donet',1:'Line',2:'Pie',3:'Pizza',4:'Pie',5:'Hybrid1',6:'Hybrid2'}
		global i 
		if i>6:
			i=0
		else:
			self.ui.widget.rpb_setBarStyle(dic[i])
			i+=1


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
