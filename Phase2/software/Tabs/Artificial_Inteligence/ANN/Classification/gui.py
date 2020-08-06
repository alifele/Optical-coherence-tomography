from PyQt5 import QtWidgets
from Tabs.Artificial_Inteligence.ANN.Classification.main import Ui_Dialog
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
        self.ui.label.pixmap().fill(QtGui.QColor('black'))

        self.ui.spinBox.valueChanged.connect(self.layers_chaged)
        self.ui.spinBox.setValue(int(4))
        self.ui.pushButton_2.clicked.connect(self.start_train)
        self.ui.pushButton.clicked.connect(self.predict)
        self.ui.push_clear.clicked.connect(self.clear_canv)

    def predict(self):
        self.ui.label.pixmap().save('log/handwritten.png')
        image = imageio.imread('log/handwritten.png')
        plt.imshow(image)
        plt.show()


    def clear_canv(self):
        self.ui.label.pixmap().fill(QtGui.QColor('black'))
        self.ui.label.update()

    def layers_chaged(self, val):
        self.ui.tableWidget.setRowCount(int(val))
        for i in range(val):
            item = QtWidgets.QTableWidgetItem('layer{}'.format(i+1))
            self.ui.tableWidget.setVerticalHeaderItem(i, item)


    def start_train(self):
        number_of_neurons_list = []
        for i in range(int(self.ui.spinBox.text())):
            number_of_neurons_list.append(int(self.ui.tableWidget.item(i,0).text()))






class classification_gui(classification):
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
