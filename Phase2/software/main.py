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
import sys

from Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.gui import huxly_dialog
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.gui import fitz_dialog
from Tabs.Dynamical_systems.neuron_models.costum.Implementation.gui import cos_dialog

from Tabs.Dynamical_systems.neuron_models.About_us.gui import aboutus_gui

from Tabs.Artificial_Inteligence.ANN.Classification.gui import classification_gui



from appear import UI_elemts





class mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI_elemts()
        self.ui.Setup_UI(self)

        self.init_signals()





    def init_signals(self):
        self.ui.dynamic_tab.huxly_model.triggered.connect(self.huxly_clicked)
        self.ui.dynamic_tab.Fithz.triggered.connect(self.fitz_clicked)
        self.ui.artificial_intelligence_tab.class_.triggered.connect(self.classifi_clikced)



    def huxly_clicked(self):
        self.huxly_window = huxly_dialog(self.ui)

    def fitz_clicked(self):
        self.classi_window = cos_dialog(self.ui)

        self.fitz_window = fitz_dialog(self.ui)

    def classifi_clikced(self):
        self.classi_window = aboutus_gui(self.ui)
        self.classi_window = cos_dialog(self.ui)

    def about_clikced(self):
        self.about = aboutus_gui(self.ui)




def start():
    app = QApplication([])
    main = mainwindow()
    #main.test()
    main.show()
    sys.exit(app.exec_())

start()
