

import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

from PyQt5 import QtCore, QtGui, QtWidgets

from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.functions import *
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.plotutils import *
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.variables import *
from Tabs.Dynamical_systems.neuron_models.Fithz.Implementation.animutils import Animationcls


class Canvas(FigureCanvasQTAgg):
    def __init__(self,shapes=[221,222,224], parent=None, width=50, height=20, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.patch.set_facecolor('#19232D')
        self.fig.subplots_adjust(top=0.94,
                                bottom=0.109,
                                left=0.067,
                                right=0.962,
                                hspace=0.343,
                                wspace=0.197)

        #ax = fig.add_subplot(4,4,(1,16))
        #ax.set_yticks([])
        #ax.axis('off')

        I =  10

        self.ax1 = self.fig.add_subplot(3,3,(1,8))
        self.ax1.set_xlabel('w')
        self.ax1.set_ylabel('v')
        self.ax1.tick_params(axis='x', colors='#5e6f80', labelsize=7)
        self.ax1.tick_params(axis='y', colors='#5e6f80', labelsize=7)
        self.ax1.set_facecolor("#c6c9cc")
        self.phase_line, = self.ax1.plot([],[],'ro')

        self.ax2 = self.fig.add_subplot(3,3,3, title = 'v_plot')
        self.ax2.set_xlim([0,t_total])
        self.ax2.set_ylim([-2,2])
        self.ax2.set_ylabel('v')
        self.ax2.set_xlabel('t')
        self.ax2.tick_params(axis='x', colors='#5e6f80', labelsize=7)
        self.ax2.tick_params(axis='y', colors='#5e6f80', labelsize=7)
        self.ax2.set_facecolor("#c6c9cc")
        self.v_track, = self.ax2.plot([],[])


        self.ax3 = self.fig.add_subplot(3,3,9, title = 'w_plot')
        self.ax3.set_xlim([0,t_total])
        self.ax3.set_ylim([-2,2])
        self.ax3.set_ylabel('w')
        self.ax3.set_xlabel('t')
        #ax.autoscale_view(scaley=True)
        self.ax3.autoscale(axis='y')
        self.ax3.tick_params(axis='x', colors='#5e6f80', labelsize=7)
        self.ax3.tick_params(axis='y', colors='#5e6f80', labelsize=7)
        self.ax3.set_facecolor("#c6c9cc")
        self.w_track, = self.ax3.plot([],[])


        self.ax4 = self.fig.add_subplot(3,3,6)
        self.ax4.text(0,0,'I = {}'.format(I), fontsize=12, horizontalalignment='center', verticalalignment = 'center')
        self.ax4.set_xlim([-0.5,0.5])
        self.ax4.set_ylim([-0.5,0.5])
        self.ax4.set_facecolor("#19232D")
        self.ax4.set_axis_off()

        super().__init__(self.fig)



class canvas_widget(QtWidgets.QWidget):
    def __init__(self, centralwidget):
        super(QtWidgets.QWidget, self).__init__(centralwidget)

        self.canvas = Canvas()

        layout = QtWidgets.QVBoxLayout()
        toolbar = NavigationToolbar2QT(self.canvas, self)
        layout.addWidget(toolbar)
        layout.addWidget(self.canvas)

        self.setGeometry(QtCore.QRect(349, 180, 300, 400))
        self.setObjectName("widget")
        self.setLayout(layout)
