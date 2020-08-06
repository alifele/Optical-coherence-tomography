from PyQt5 import QtWidgets
from .main import Ui_Dialog
import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtGui
import imageio
import numpy as np
import matplotlib.pyplot as plt


class classification(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)






class aboutus_gui(classification):
    def __init__(self, ui):
        super().__init__()
        self.setWindowTitle('Fitz-Hugh Nagumo model')
        ui.mdiArea.addSubWindow(self)
        self.exec_()


if __name__ == '__main__':
    from main import Ui_Dialog
    app = QtWidgets.QApplication([])
    window = huxly()
    window.show()
    app.exec_()
