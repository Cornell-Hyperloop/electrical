from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pyqtgraph.exporters


class PlotButtons(QWidget):
    def __init__(self, plot):
        super(PlotButtons, self).__init__(None)
        self.plot = plot
        self.plot_reset = False
        # self.exporter = pyqtgraph.exporters.ImageExporter(
        #     self.plot.scene())
        # self.exporter.parameters()['width'] = 1372
        # self.exporter.parameters()['height'] = 639
        # self.exporter.parameters()['width'], \
        #     self.exporter.parameters()['height'] = \
        #     self.plot.frameGeometry().width(), self.plot.frameGeometry().height()
        self.current_plot = 0
        self.plot_names = ['Plot 1', 'Plot 2']
        self.changed_plot = False
        self.rescale_axes = False
        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout()

        # Reset plot button
        self.reset_plot_button = QPushButton(self)
        self.reset_plot_button.setText("Reset Plot")
        self.reset_plot_button.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.reset_plot_button.clicked.connect(self.resetPlot)

        self.export_button = QPushButton(self)
        self.export_button.setText("Export Graph")
        self.export_button.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.export_button.clicked.connect(self.exportGraph)

        self.plot_dropdown = QComboBox()
        self.plot_dropdown.setEditable(True)
        self.plot_dropdown.lineEdit().setAlignment(Qt.AlignCenter)
        self.plot_dropdown.lineEdit().setReadOnly(True)
        for plot_name in self.plot_names:
            self.plot_dropdown.addItem(plot_name)
        self.plot_dropdown.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1;")
        self.plot_dropdown.currentTextChanged.connect(self.plotDropdownChanged)

        hbox.addWidget(self.reset_plot_button)
        hbox.addWidget(self.export_button)
        hbox.addWidget(self.plot_dropdown)

        # Add the widget for resizing the plot axes
        resize_input_widgets = QSplitter(Qt.Vertical)
        row1 = QSplitter(Qt.Horizontal)
        row2 = QSplitter(Qt.Horizontal)
        row3 = QSplitter(Qt.Horizontal)

        self.textbox1 = QLineEdit(self)
        self.textbox1.resize(100, 100)
        self.textbox1.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.textbox2 = QLineEdit(self)
        self.textbox2.resize(100, 100)
        self.textbox2.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.textbox3 = QLineEdit(self)
        self.textbox3.resize(100, 100)
        self.textbox3.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.textbox4 = QLineEdit(self)
        self.textbox4.resize(100, 100)
        self.textbox4.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")

        self.rescale_axes_button = QPushButton(self)
        self.rescale_axes_button.setText("Rescale Axes")
        self.rescale_axes_button.setStyleSheet(
            "font-family: Helvetica; font-size: 14px; background-color : #2B26c1")
        self.rescale_axes_button.clicked.connect(self.rescaleAxes)

        row1.addWidget(self.textbox1)
        row1.addWidget(self.textbox2)
        row2.addWidget(self.textbox3)
        row2.addWidget(self.textbox4)
        row3.addWidget(self.rescale_axes_button)

        resize_input_widgets.addWidget(row1)
        resize_input_widgets.addWidget(row2)
        resize_input_widgets.addWidget(row3)

        hbox.addWidget(self.reset_plot_button)
        hbox.addWidget(self.export_button)
        hbox.addWidget(resize_input_widgets)
        self.setLayout(hbox)

    def resetPlot(self):
        self.plot.clear()
        self.plot_reset = True

    def setPlotResetFlag(self, flag):
        self.plot_reset = flag

    def getPlotResetFlag(self):
        return self.plot_reset

    def exportGraph(self):
        self.plot.getPlotItem().writeImage("Graph.png")
        # self.exporter.export('Graph.png')

    def plotDropdownChanged(self, dropdownValue):
        self.current_plot = self.plot_names.index(dropdownValue)
        self.changed_plot = True

    def getCurrentPlot(self):
        return self.current_plot

    def getChangedPlot(self):
        return self.changed_plot

    def setChangedPlot(self, newValue):
        self.changed_plot = newValue

    def rescaleAxes(self):
        self.x_min = int(self.textbox1.text())
        self.x_max = int(self.textbox2.text())
        self.y_min = int(self.textbox3.text())
        self.y_max = int(self.textbox4.text())
        self.rescale_axes = True

    def getRescaleAxesFlag(self):
        return self.rescale_axes

    def setRescaleAxesFlag(self, flag):
        self.rescale_axes = flag

    def getXAxesLimits(self):
        return [self.x_min, self.x_max]

    def getYAxesLimits(self):
        return [self.y_min, self.y_max]
