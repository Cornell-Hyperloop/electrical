from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .fsm import FSM
import sys


class EmergencyButton(QWidget):
    def __init__(self, fsm, parent=None):
        super(EmergencyButton, self).__init__(parent)
        self.fsm = fsm
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Click button")
        self.push = QPushButton(self)
        self.push.setText("Emergency\nBreak")
        self.push.setFont(QFont('AnyStyle', 18))
        self.push.clicked.connect(self.pushedEmergency)
        #self.push.resize(400, 200)
        #self.push.move(0, 50)
        self.push.setStyleSheet(
            "background-color : red; border-radius: 5px; font-weight: bold; border: 3px solid black")
        # sshFile = "test.css"
        # with open(sshFile, "r") as fh:
        #     self.push.setStyleSheet(fh.read())

    def msgButtonClick(self, i):
        print("Button clicked is:", i.text())

    def pushedEmergency(self):
        # self.msgBox = QMessageBox()
        # self.msgBox.setIcon(QMessageBox.Information)
        # self.msgBox.setText("Do you want to terminate program?")
        # self.msgBox.setWindowTitle("Emergency Button Pushed!")
        # self.msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # self.msgBox.buttonClicked.connect(self.msgButtonClick)

        # returnValue = self.msgBox.exec()
        # if returnValue == QMessageBox.Ok:
        #     print('OK clicked')
        #     sys.exit()
        # else:
        #     print("Action cancelled")

        self.fsm.fsm.setState('Emergency')
