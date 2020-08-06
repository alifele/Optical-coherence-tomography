from PyQt5 import QtWidgets
from .main import Ui_Dialog
import numpy as np
import matplotlib.pyplot as plt
from Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.Simulator_functions import *
import Tabs.Dynamical_systems.neuron_models.Huxly.Implementation.variables as var
from .animutils import Animationcls
from .animation_run import run_animation


class huxly(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()

        self.ui  = Ui_Dialog()
        self.ui.setupUi(self)

        self.signals_init()

        self.ui.verticalSlider.setMaximum(50)
        self.ui.verticalSlider.setMinimum(-5)
        self.ui.verticalSlider.setSingleStep(0.1)

        self.ui.lineEdit.setText(str(self.ui.verticalSlider.value()))


        self.run_the_simu()

    def closeEvent(self, event):
        self.anim._stop()


    def signals_init(self):
        self.ui.verticalSlider.valueChanged.connect(self.slider_changed)
        self.ui.lineEdit.returnPressed.connect(self.lineEditChanged)

    def run_the_simu(self):
        self.I = float(self.ui.lineEdit.text())
        v = -63
        n = 0
        m = 0
        h = 0
        dt = 0.001
        t_total = 10
        t = np.arange(0, t_total, dt)
        self.t = t

        self.v_list, self.n_list, self.m_list, self.h_list, self.N_spikes = experiment_run(v,n,m,h,self.I,t_total, dt)
        self.run_animation()


    def run_animation(self):

        self.ui.widget.canvas.ax1.plot(self.t, self.v_list,'--',alpha=0.5, label='v_list')
        self.ui.widget.canvas.ax1.set_xticks([])
        self.ui.widget.canvas.ax1.set_ylabel('V')

        self.ui.widget.canvas.ax2.plot(self.t, self.n_list,'--',alpha=0.5, label='n_list')
        self.ui.widget.canvas.ax2.set_xticks([])
        self.ui.widget.canvas.ax2.set_ylabel('n')

        self.ui.widget.canvas.ax3.plot(self.t, self.h_list,'--',alpha=0.5, label='h_list')
        self.ui.widget.canvas.ax3.set_xticks([])
        self.ui.widget.canvas.ax3.set_ylabel('h')

        self.ui.widget.canvas.ax4.plot(self.t, self.m_list,'--',alpha=0.5, label='h_list')
        self.ui.widget.canvas.ax4.set_ylabel('m')
        self.ui.widget.canvas.ax4.set_xlabel('t ($ms$)')

        self.ui.widget.canvas.ax5.plot(self.n_list, self.v_list, '--')
        self.ui.widget.canvas.ax5.set_xlabel('n')
        self.ui.widget.canvas.ax5.set_ylabel('v')

        Lines = [self.ui.widget.canvas.line1
                ,self.ui.widget.canvas.line2
                ,self.ui.widget.canvas.line3
                ,self.ui.widget.canvas.line4
                ,self.ui.widget.canvas.line5]

        Pathes = [[self.t, self.v_list]
                ,[self.t, self.n_list]
                ,[self.t,self.h_list]
                ,[self.t,self.m_list]
                ,[self.n_list,self.v_list]]

        init_data = [[self.t[0],self.v_list[0]]
                    ,[self.t[0],self.n_list[0]]
                    ,[self.t[0],self.h_list[0]]
                    ,[self.t[0],self.m_list[0]]
                    ,[self.n_list[0],self.v_list[0]]]

        draw_mode = ['line', 'line','line', 'line', 'dot']

        animobj = Animationcls(Lines, Pathes, init_data, self.ui.widget.canvas.fig, draw_mode)
        self.anim = animobj.start_animation()

    def slider_changed(self, value):
        self.ui.lineEdit.setText(str(value))
        self.anim._stop()
        self.clear_axes()
        self.run_the_simu()

    def lineEditChanged(self):
        value = self.ui.lineEdit.text()
        self.ui.verticalSlider.setValue(float(value))
        self.anim._stop()
        self.clear_axes()
        self.run_the_simu()

    def clear_axes(self):
        self.ui.widget.canvas.ax1.clear()
        self.ui.widget.canvas.ax2.clear()
        self.ui.widget.canvas.ax3.clear()
        self.ui.widget.canvas.ax4.clear()
        self.ui.widget.canvas.ax5.clear()





class huxly_dialog(huxly):
    def __init__(self, ui):
        super().__init__()
        self.setWindowTitle('Sin plotter')
        ui.mdiArea.addSubWindow(self)
        self.exec_()


if __name__ == '__main__':
    from main import Ui_Dialog
    app = QtWidgets.QApplication([])
    window = huxly()
    window.show()
    app.exec_()
