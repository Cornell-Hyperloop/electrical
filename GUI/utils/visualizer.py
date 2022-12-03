from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *


class Visualizer(QWidget):
    def __init__(self, *args, **kwargs):
        super(Visualizer, self).__init__()

        pod1 = Pod(True)
        pod2 = Pod(True)
        pod3 = Pod(True)
        pod4 = Pod(True)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox1.addWidget(pod1)
        hbox1.addWidget(pod2)
        hbox2.addWidget(pod3)
        hbox2.addWidget(pod4)

        vbox = QVBoxLayout()

        #self.setLayout(hbox)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)


        self.setLayout(vbox)
