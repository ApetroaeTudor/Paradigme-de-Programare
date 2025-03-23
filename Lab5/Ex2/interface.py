import subprocess

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication,QPushButton,QLabel,QMainWindow,QWidget
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QRect, QPoint, QTimer, QEvent

from gameEngine import MyGame
import constants as c

import functions as fn

import msgQueue as mq

from multiprocessing import Process,Queue

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
        self.move(50,50)
        self.setParent(parentWidget)


class GameInterface(QMainWindow):
    gameEngine:MyGame

    playerNr=-1



    def __init__(self,game,loginQueue:Queue,movesQueue:Queue,loggedUsersQueue:Queue):
        super().__init__()

        self.loggedUsersQueue=loggedUsersQueue
        self.myGameEngine=game
        self.loginQueue=loginQueue
        self.movesQueue=movesQueue

        self.myUsername=""


        #SETUP MAIN WINDOW
        self.myBaseWidget=QWidget()
        self.myBaseWidget.setStyleSheet("background: #2e2e2e")
        self.myBaseWidget.setFixedSize(QSize(c.WINDOW_WIDTH,c.WINDOW_HEIGHT))
        self.setWindowTitle("XO")
        self.setCentralWidget(self.myBaseWidget)
        self.myBaseWidget.setParent(self)


        #LOGO
        self.myLogoLabel=QLabel()
        self.myLogoLabel.setFixedSize(QSize(500,100))
        self.myLogoLabel.setPixmap(QPixmap("res/TicTacToe.png"))
        self.myLogoLabel.setScaledContents(True)
        self.myLogoLabel.setParent(self.myBaseWidget)
        self.myLogoLabel.move(850,100)

        # #MY NAME LABEL
        self.myNameLabel = QLabel()
        self.myNameLabel.setStyleSheet("color: white")
        self.myNameLabel.setFont(QFont("Helvetica", 20))
        self.myNameLabel.setFixedSize(QSize(500,40))
        self.myNameLabel.setParent(self.myBaseWidget)
        self.myNameLabel.move(30, 10)

        #SCORE LABEL
        self.myScoreLabel=QLabel()
        self.myScoreLabel.setStyleSheet("color: white")
        self.myScoreLabel.setFont(QFont("Helvetica",20))
        self.myScoreLabel.setText("Score:")
        self.myScoreLabel.setParent(self.myBaseWidget)
        self.myScoreLabel.move(900,200)

        #SETUP GAME
        self.myLabelGameFrame=GameLabel(self.myBaseWidget)
        self.myLabelGameFrame.myBtnList=fn.initButtonsForGame(self.myLabelGameFrame,self.myGameEngine.getGameState(),self)
        #doar initializez butoanele, nu le si aleg layout-ul


        #TIMER FOR UPDATES
        self.myUpdateTimer=QTimer()
        self.myUpdateTimer.timeout.connect(lambda:self.updateUI())
        self.myUpdateTimer.timeout.connect(lambda:self.processQueue())
        self.myUpdateTimer.start(100)


    def processQueue(self):
        if self.playerNr==-1:
            try:
                msg=self.loginQueue.get_nowait()
                if str(msg).split(".")[0]=="ASSIGN_PLAYER":
                    self.playerNr=str(msg).split(".")[1]
                    self.setWindowTitle("XO-Player"+str(self.playerNr))
                else:
                    self.loginQueue.put(msg)
            except:
                pass

        try:
            msg = self.movesQueue.get_nowait()
            if str(msg).split(".")[0]=="MOVE":
                move=str(msg).split(".")[1]
                row = int(str(move)[0])
                col = int(str(move)[1])
                if int(self.playerNr)==int(self.myGameEngine.getTurn()):
                    self.myGameEngine.takeMoveFromPlayer(row,col)
        except:
            pass

    def updateUI(self):
        if self.myUsername!="":

            self.myNameLabel.setText("Username: "+self.myUsername)
        for i in range(3):
            for j in range(3):
                for btnList in self.myLabelGameFrame.myBtnList:
                    for btn in btnList:
                        if btn.correspondingPosition == f"{i}{j}":
                            if not self.myGameEngine.getGameState()[i][j] =='-':
                                btn.updateBtnText(self.myGameEngine.getGameState()[i][j])

        gamestate=self.myGameEngine.checkCurrentState()
        if gamestate[0]==0:
            self.myUpdateTimer.stop()
            if gamestate[1]==0:
                print("X WINS")
            elif gamestate[1]==1:
                print("O WINS")
            elif gamestate[1]==2:
                print("TIE")

    def toggleOn(self):
        self.show()
    def toggleOff(self):
        self.hide()

    def getEngine(self):
        return self.myGameEngine


        
        
