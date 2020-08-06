

import sys
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

from PyQt5 import QtCore, QtGui, QtWidgets


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

        self.ax1 = self.fig.add_subplot(6,4,(1,4), title = 'I = {} $nAmp$'.format(I))
        self.ax1.tick_params(axis='x', colors='#5e6f80', labelsize=7)
        self.ax1.tick_params(axis='y', colors='#5e6f80', labelsize=7)
        self.ax1.set_facecolor("#c6c9cc")
        self.line1, = self.ax1.plot([],[],lw=3)


        self.ax2 = self.fig.add_subplot(6,4,(5,8))
        self.ax2.tick_params(axis='x', colors='#5e6f80', labelsize=7)
        self.ax2.tick_params(axis='y', colors='#5e6f80', labelsize=7)
        self.ax2.set_facecolor("#c6c9cc")
        self.line2, = self.ax2.plot([],[],lw=3)

        self.ax3 = self.fig.add_subplot(6,4,(9,12))
        self.ax3.tick_params(axis='x', colors='#5e6f80', labelsize=7)
        self.ax3.tick_params(axis='y', colors='#5e6f80', labelsize=7)
        self.ax3.set_facecolor("#c6c9cc")
        self.line3, = self.ax3.plot([],[],lw=3)


        self.ax4 = self.fig.add_subplot(6,4,(13,16))
        self.ax4.tick_params(axis='x', colors='#5e6f80', labelsize=7)
        self.ax4.tick_params(axis='y', colors='#5e6f80', labelsize=7)
        self.ax4.set_facecolor("#c6c9cc")
        self.line4, = self.ax4.plot([],[],lw=3)

        #fig = plt.figure()
        self.ax5 = self.fig.add_subplot(6,4,(17,24))
        self.ax5.tick_params(axis='x', colors='#5e6f80', labelsize=7)
        self.ax5.tick_params(axis='y', colors='#5e6f80', labelsize=7)
        self.ax5.set_facecolor("#c6c9cc")
        self.line5, = self.ax5.plot([],[],'ro')

        super().__init__(self.fig)


    def run_animation(v_list, n_list, m_list, h_list, N_spikes,I,t):




        Lines = [line1, line2, line3, line4, line5]
        Pathes = [[t, v_list], [t, n_list],[t,h_list],[t,m_list],[n_list,v_list]]
        init_data = [[t[0], v_list[0]],[t[0], n_list[0]],[t[0],h_list[0]],[t[0],m_list[0]],[n_list[0],v_list[0]]]
        draw_mode = ['line', 'line','line', 'line', 'dot']



        animobj = Animationcls(Lines, Pathes, init_data, fig, draw_mode)
        anim = animobj.start_animation()
        anim.save('result{}'.format(0) + '.gif', dpi=100, writer='imagemagick', fps = 30)



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
