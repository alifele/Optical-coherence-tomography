from imports import *
from PyQt5 import QtWidgets


class Actions_cls:
    def __init__(self, mainwindow):
        self.huxly_model = QtWidgets.QAction(QIcon('icons/icon.png'),"Huxly", mainwindow)
        self.Fithz = QtWidgets.QAction(QIcon('icons/icon.png'),"Fithz", mainwindow)
        self.custom = QtWidgets.QAction(QIcon('icons/icon.png'),"custom", mainwindow)
        self._brain_action = QtWidgets.QAction(QIcon('icons/icon.png'),"Brain", mainwindow)

        self.model = QtWidgets.QAction(QIcon('icons/icon.png'),"perceptro", mainwindow)
        self.multi = QtWidgets.QAction(QIcon('icons/icon.png'),"Multi", mainwindow)
        self.hop = QtWidgets.QAction(QIcon('icons/icon.png'),"Hoppfild", mainwindow)
        self.heb = QtWidgets.QAction(QIcon('icons/icon.png'),"Hebb", mainwindow)
        self.som = QtWidgets.QAction(QIcon('icons/icon.png'),"self orga. map", mainwindow)

        self.class_ = QtWidgets.QAction(QIcon('icons/icon.png'),"classifi", mainwindow)
        self.reg = QtWidgets.QAction(QIcon('icons/icon.png'),"Regress", mainwindow)
        self.gan = QtWidgets.QAction(QIcon('icons/icon.png'),"GAN", mainwindow)
        self.cnn = QtWidgets.QAction(QIcon('icons/icon.png'),"CNN", mainwindow)
        self.rnn = QtWidgets.QAction(QIcon('icons/icon.png'),"RNN", mainwindow)
        self.maze = QtWidgets.QAction(QIcon('icons/icon.png'),"maze", mainwindow)
        self.snake = QtWidgets.QAction(QIcon('icons/icon.png'),"snake", mainwindow)
        self.pingpong = QtWidgets.QAction(QIcon('icons/icon.png'),"pingpong", mainwindow)
        self.genet = QtWidgets.QAction(QIcon('icons/icon.png'),"toward goal", mainwindow)
        self.mona = QtWidgets.QAction(QIcon('icons/icon.png'),"Monaliza", mainwindow)
        self.car = QtWidgets.QAction(QIcon('icons/icon.png'),"car", mainwindow)
        self.cond = QtWidgets.QAction(QIcon('icons/icon.png'),"Conditioning", mainwindow)
