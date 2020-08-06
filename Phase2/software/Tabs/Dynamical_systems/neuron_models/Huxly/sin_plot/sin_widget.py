from PyQt5 import QtWidgets

from Tabs.Dynamical_systems.neuron_models.Huxly.sin_plot.main_sin import Ui_Form
from Tabs.Dynamical_systems.neuron_models.Huxly.sin_plot.plot import canvas_widget
import numpy as np





class Sin_window(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        t = np.arange(0,10,0.1)
        self.line, = self.ui.widget.canvas.axes[0].plot(t,np.sin(t))


        self.ui.amp_slider.valueChanged.connect(self.plotter)
        self.ui.freq_slider.valueChanged.connect(self.plotter)



    def plotter(self, value):
        t = np.arange(0,10,0.1)
        amp = self.ui.amp_slider.value()
        freq = self.ui.freq_slider.value()
        self.ui.widget.canvas.axes[0].clear()
        self.ui.widget.canvas.axes[0].plot(t,amp*np.sin(t*freq) )
        self.ui.amp_lineEdit.setText(str(amp))
        self.ui.freq_line_Edit.setText(str(freq))

        #self.line.set_ydata(value*np.sin(t))
        self.ui.widget.canvas.draw()




class sinWidget(Sin_window):
    def __init__(self, ui):
        super().__init__()
        self.setWindowTitle('Sin plotter')
        ui.mdiArea.addSubWindow(self)
        self.exec_()
