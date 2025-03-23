from PyQt5.QtWidgets import QApplication,QPushButton,QLabel,QMainWindow,QWidget
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QRect, QPoint, QTimer, QEvent

from gameEngine import MyGame
import constants as c

import functions as fn

import sys

class GameInterface(QMainWindow):
    gameEngine=MyGame()

    def __init__(self):
        super().__init__()

        #SETUP MAIN WINDOW
        self.myBaseWidget=QWidget()
        self.myBaseWidget.setFixedSize(QSize(c.WINDOW_WIDTH,c.WINDOW_HEIGHT))
        self.setWindowTitle("XO")
        self.setCentralWidget(self.myBaseWidget)


        #SETUP GAME
        self.myLabelGameFrame=QLabel()
        self.myLabelGameFrame.setFixedSize(QSize(c.GAME_HEIGHT,c.GAME_WIDTH))
        self.myLabelGameFrame.setParent(self.myBaseWidget)
        self.myLabelGameFrame.move(300,50)
        self.myBtnList=fn.initButtonsForGame(self.myLabelGameFrame)


        #TIMER FOR UPDATES
        self.myUpdateTimer=QTimer()
        self.myUpdateTimer.timeout.connect(lambda:self.updateUI())
        self.myUpdateTimer.start(200)

    def updateUI(self):
        pass
        #fn.deleteButtonsForGame(self.myLabelGameFrame)
        #self.myBtnList=fn.initButtonsForGame(self.myLabelGameFrame)

        
        
