# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledPXqcAq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("CIRCULAR PROGRESS BAR - PyQT5")
        MainWindow.setFixedSize(1020, 680)
        MainWindow.setStyleSheet(u"")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -20, 1021, 731))
        self.label.setStyleSheet(u"QLabel\n"
"{\n"
"background-color: #291F31;\n"
"\n"
"}")
        self.widget = roundProgressBar(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(340, 140, 351, 321))

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(460, 520, 93, 28))

        self.pushButton1 = QPushButton(self.centralwidget)
        self.pushButton1.setObjectName(u"pushButton")
        self.pushButton1.setGeometry(QRect(460, 550, 93, 28))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        
        self.label.setText("")
        self.pushButton.setText("CLICK ME")
        self.pushButton1.setText('Change Theme')
    # retranslateUi

