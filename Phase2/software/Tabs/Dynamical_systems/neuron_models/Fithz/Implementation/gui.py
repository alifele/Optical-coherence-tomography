from PyQt5 import QtWidgets
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.main import Ui_Dialog
import numpy as np
import matplotlib.pyplot as plt
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.variables import *
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.functions import *
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.animutils import Animationcls
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.plotutils import *



class Fitz(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.ui  = Ui_Dialog()
        self.ui.setupUi(self)

        self.signals_init()

        self.ui.verticalSlider.setMaximum(120)
        self.ui.verticalSlider.setMinimum(-100)
        self.ui.verticalSlider.setSingleStep(0.1)

        self.ui.lineEdit.setText(str(self.ui.verticalSlider.value()/100))


        self.run_the_simu()

    def closeEvent(self, event):
        self.anim._stop()


    def signals_init(self):
        self.ui.verticalSlider.valueChanged.connect(self.slider_changed)
        self.ui.lineEdit.returnPressed.connect(self.lineEditChanged)

    def run_the_simu(self):
        self.I = float(self.ui.lineEdit.text())

        self.v_list, self.w_list, self.v_dot_list, self.w_dot_list = run_experiment(v,w,self.I,t_total, dt)
        self.run_animation()


    def run_animation(self):

        self.ui.widget.canvas.ax1.plot(self.w_list,self.v_list, lw=3)
        arrow_plotter(v_range, w_range,self.I,self.ui.widget.canvas.ax1,n=50)


        self.ui.widget.canvas.ax2.set_xlim([0,t_total])
        self.ui.widget.canvas.ax2.set_ylim([-2,2])

        self.ui.widget.canvas.ax3.set_xlim([0,t_total])
        self.ui.widget.canvas.ax3.set_ylim([-2,2])
        self.ui.widget.canvas.ax3.autoscale(axis='y')

        self.ui.widget.canvas.ax4.text(0,0,'I = {}'.format(self.I), fontsize=12, horizontalalignment='center', verticalalignment = 'center')
        self.ui.widget.canvas.ax4.set_xlim([-0.5,0.5])
        self.ui.widget.canvas.ax4.set_ylim([-0.5,0.5])
        self.ui.widget.canvas.ax4.set_facecolor("#19232D")



        Lines = [self.ui.widget.canvas.phase_line
                ,self.ui.widget.canvas.v_track
                ,self.ui.widget.canvas.w_track]

        Pathes = [[self.w_list, self.v_list]
                ,[t, self.v_list]
                ,[t,self.w_list]]

        initial = [[self.w_list[0], self.v_list[0]]
                    ,[t[0], self.v_list[0]]
                    ,[t[0],self.w_list[0]]]

        draw_mode = ['dot','line','line']

        animobj = Animationcls(Lines, Pathes, initial, self.ui.widget.canvas.fig, draw_mode)
        self.anim = animobj.start_animation()



    def slider_changed(self, value):
        self.ui.lineEdit.setText(str(value/100))
        self.anim._stop()
        self.clear_axes()
        self.run_the_simu()

    def lineEditChanged(self):
        value = self.ui.lineEdit.text()
        self.ui.verticalSlider.setValue(float(value)*100)
        self.anim._stop()
        self.clear_axes()
        self.run_the_simu()

    def clear_axes(self):
        self.ui.widget.canvas.ax1.clear()
        self.ui.widget.canvas.ax2.clear()
        self.ui.widget.canvas.ax3.clear()
        self.ui.widget.canvas.ax4.clear()





class fitz_dialog(Fitz):
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
