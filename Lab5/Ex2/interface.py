from PyQt5.QtWidgets import QApplication,QPushButton,QLabel,QMainWindow,QWidget
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QRect, QPoint, QTimer, QEvent

from gameEngine import MyGame
import constants as c

import functions as fn

import msgQueue as mq

import sys


class GameButton(QPushButton):
    correspondingPosition:str
    btnText:str
    def __init__(self,position:str,width:int,height:int,parentWidget:QWidget,root:QMainWindow):
        super().__init__()
        self.correspondingPosition=position
        self.setFixedSize(QSize(width,height))
        self.setParent(parentWidget)
        self.root=root

    def updateBtnText(self,text:str):
        self.btnText=text
        self.setText(text)

class GameLabel(QLabel):
    myBtnList:list[GameButton]
    def __init__(self,parentWidget:QWidget):
        super().__init__()
        self.setFixedSize(QSize(c.GAME_HEIGHT,c.GAME_WIDTH))
        self.move(300,50)
        self.setParent(parentWidget)


class GameInterface(QMainWindow):
    gameEngine:MyGame

    def __init__(self):
        super().__init__()

        self.gameEngine=MyGame()

        #SETUP MAIN WINDOW
        self.myBaseWidget=QWidget()
        self.myBaseWidget.setFixedSize(QSize(c.WINDOW_WIDTH,c.WINDOW_HEIGHT))
        self.setWindowTitle("XO")
        self.setCentralWidget(self.myBaseWidget)
        self.myBaseWidget.setParent(self)


        #SETUP GAME
        self.myLabelGameFrame=GameLabel(self.myBaseWidget)
        self.myLabelGameFrame.myBtnList=fn.initButtonsForGame(self.myLabelGameFrame,self.gameEngine.currentState,self)


        #TIMER FOR UPDATES
        self.myUpdateTimer=QTimer()
        self.myUpdateTimer.timeout.connect(lambda:self.updateUI())
        self.myUpdateTimer.timeout.connect(lambda:self.processQueue())
        self.myUpdateTimer.start(100)


    def processQueue(self):
        try:
            move = mq.asyncQueue.get_nowait()
            row = int(str(move)[0])
            col = int(str(move)[1])
            self.gameEngine.takeMoveFromPlayer(row,col)
        except:
            pass

    def updateUI(self):
        for i in range(3):
            for j in range(3):
                for btnList in self.myLabelGameFrame.myBtnList:
                    for btn in btnList:
                        if btn.correspondingPosition == f"{i}{j}":
                            if not self.gameEngine.currentState[i][j] =='-':
                                btn.updateBtnText(self.gameEngine.currentState[i][j])

        gamestate=self.gameEngine.checkCurrentState()
        if gamestate[0]==0:
            self.myUpdateTimer.stop()
            if gamestate[1]==0:
                print("X WINS")
            elif gamestate[1]==1:
                print("O WINS")
            elif gamestate[1]==2:
                print("TIE")


        
        
