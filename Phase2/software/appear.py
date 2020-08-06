from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import QKeySequence as QKSec
from Ribbon.RibbonButton import RibbonButton
from Ribbon.Icons import get_icon
from Ribbon.RibbonTextbox import RibbonTextbox
from Ribbon.RibbonWidget import *
import qdarkstyle
from PyQt5.QtGui import QIcon
import ribbon_actions
import qdarkstyle.style_rc
from sin_plot.sin_widget import Sin_window



class Mdi_Area(QtWidgets.QMdiArea):
    def __init__(self):
        super().__init__()
        self.setViewMode(QtWidgets.QMdiArea.TabbedView)
        self.setTabsClosable(True)
        self.setTabsMovable(True)






class UI_elemts:

    def Setup_UI(self,mainwindow):

        f = open("qdarkstyle/style.qss")
        style = f.read()
        f.close()

        mainwindow.resize(800,600)
        mainwindow.setWindowTitle("My Application")
        mainwindow.setStyleSheet(style)

        layout = QtWidgets.QVBoxLayout()

        self.mdiArea = Mdi_Area()
        layout.addWidget(self.mdiArea)

        self._ribbon = RibbonWidget(mainwindow)
        mainwindow.addToolBar(self._ribbon)


        self.dynamic_tab = ribbon_actions.Dynamical_Systems_tab(self._ribbon, mainwindow)
        self.neural_networks_tab = ribbon_actions.Neural_Networks_tab(self._ribbon, mainwindow)
        self.artificial_intelligence_tab = ribbon_actions.Artificial_Intelligence_tab(self._ribbon, mainwindow)
        #self.cellular_automata_tab = ribbon_actions.Cellular_Automata_tab(self._ribbon, mainwindow)
        #self.lab_tab = ribbon_actions.Lab_tab(self._ribbon, mainwindow)


        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        mainwindow.setCentralWidget(central_widget)
