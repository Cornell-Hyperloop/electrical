from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import sys
from widgets import *
from utils.header import Header
from utils.body import Body
from utils.visualizer import Visualizer
<<<<<<< HEAD
=======
from utils.batteryPage import BatteryPage
from utils.FSM import FSM
from utils import stateMachine
import constants
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        # Insert change here
        self.setWindowTitle("Hyperloop GUI")

        hbox = QHBoxLayout(self)

<<<<<<< HEAD
        # bottom = QFrame()
        # bottom.setFrameShape(QFrame.StyledPanel)
        width = 1250
        height = 900

        header = Header(w=width, h=height)
        header.b1.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b1)))
        header.b2.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b2)))
        header.b3.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b3)))
        header.b4.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b4)))

        self.Stack = QStackedWidget(self)

        body = Body()
        visualizer = Visualizer()

        self.Stack.addWidget(body)
        self.Stack.addWidget(visualizer)

        splitter4 = QSplitter(Qt.Vertical)
        splitter4.addWidget(header)

        splitter4.addWidget(self.Stack)
        splitter4.setSizes([50, 350])

        hbox.addWidget(splitter4)

=======
        width = 1250
        height = 900

        fsm = stateMachine.FSM()

        header = Header(fsm, w=int(width), h=int(height))
        header.b1.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b1)))
        header.b2.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b2)))
        header.b3.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b3)))
        header.b4.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b4)))
        header.b5.clicked.connect(
            lambda: self.renderPage(header.navbar(header.b5)))

        self.Stack = QStackedWidget(self)

        body = Body(int(width), int(height), constants.LIVE_DATA)
        visualizer = Visualizer()
        batteryPage = BatteryPage()
        fsm_page = FSM(fsm, width, height)

        self.Stack.addWidget(body)
        self.Stack.addWidget(visualizer)
        self.Stack.addWidget(batteryPage)
        # temperature page not implemented yet
        self.Stack.addWidget(Body(width, height, False))
        self.Stack.addWidget(fsm_page)

        grid = QGridLayout(self)

        grid.addWidget(header, 0, 0)
        grid.addWidget(self.Stack, 1, 0)

        hbox.addLayout(grid)

>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b
        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.setStyleSheet("background-color: #bebebe;")

<<<<<<< HEAD
        self.setGeometry(300, 300, width, height)
=======
        self.showFullScreen()
>>>>>>> 088593597150e78bab5f05267d052282c28f0e0b

    def renderPage(self, i):
        self.Stack.setCurrentIndex(i)
