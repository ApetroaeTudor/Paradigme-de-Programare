from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QTextEdit, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer, QSize, Qt
import sys
import DB_Manager as dbm

import RegisterScreen as rs
import LoginScreen as ls
import WaitingForPlayersScreen as wfp

from multiprocessing import Process,Queue

import interface

class WelcomeScreen(QMainWindow):
    authDone:bool

    myLoginScreen:ls.LoginScreen
    myRegisterScreen:rs.RegisterScreen

    myDBManager:dbm.DatabaseManager
    ERROR_QUEUE:Queue

    def __init__(self,ERROR_QUEUE:Queue,LOGIN_QUEUE:Queue,LOGGED_USERS_QUEUE:Queue,game:interface.GameInterface):
        super().__init__()

        self.authDone=False

        self.myUsername=""


        self.MAIN_GAME=game

        self.LOGIN_QUEUE=LOGIN_QUEUE
        self.ERROR_QUEUE=ERROR_QUEUE
        self.myDBManager=dbm.DatabaseManager(self.ERROR_QUEUE)
        self.myLoginScreen = ls.LoginScreen(self.myDBManager,ERROR_QUEUE,LOGGED_USERS_QUEUE)
        self.myRegisterScreen = rs.RegisterScreen(self.myDBManager,ERROR_QUEUE,LOGGED_USERS_QUEUE)
        self.myWaitingForPlayersScreen = wfp.WaitingForPlayersWindow()

        #MAIN SETUP
        self.setWindowTitle("Log-in")
        self.myMainWidget=QWidget(); self.myMainWidget.setFixedSize(400,500); self.setCentralWidget(self.myMainWidget)
        self.myMainWidget.setStyleSheet("background-color: #2e2e2e ")

        #HBOXES
        self.myHBoxLayout1=QHBoxLayout(); self.myHBoxLayout2=QHBoxLayout(); self.myHBoxLayout3=QHBoxLayout()

        #MAIN VBOXLAYOUT
        self.myVBoxMainLayout=QVBoxLayout()
        self.myVBoxMainLayout.insertSpacing(0,20)
        self.myVBoxMainLayout.insertLayout(1,self.myHBoxLayout1)
        self.myVBoxMainLayout.insertSpacing(2,100)
        self.myVBoxMainLayout.insertLayout(3,self.myHBoxLayout2)
        self.myVBoxMainLayout.insertSpacing(4,100)
        self.myVBoxMainLayout.insertLayout(5,self.myHBoxLayout3)
        self.myVBoxMainLayout.insertStretch(6)
        self.myMainWidget.setLayout(self.myVBoxMainLayout)

        #TITLE LABEL
        self.myTitleLabel=QLabel(); self.myTitleLabel.setText("WELCOME"); self.myTitleLabel.setFont(QFont("Helvetica",23,QFont.Bold)); self.myTitleLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white; border-radius: 5px; ")
        self.myHBoxLayout1.insertWidget(0,self.myTitleLabel)
        self.myHBoxLayout1.setAlignment(Qt.AlignCenter)

        #LOGIN BUTTON
        self.myLoginButton=QPushButton(); self.myLoginButton.setText("LOG-IN"); self.myLoginButton.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white ")
        self.myLoginButton.setFixedSize(QSize(200,60))
        self.myLoginButton.clicked.connect(self.switchToLogin)
        self.myHBoxLayout2.insertWidget(0,self.myLoginButton)
        self.myHBoxLayout2.setAlignment(Qt.AlignCenter)

        #REGISTER BUTTON
        self.myRegisterButton = QPushButton(); self.myRegisterButton.setText("REGISTER"); self.myRegisterButton.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white ")
        self.myRegisterButton.setFixedSize(QSize(200,60))
        self.myRegisterButton.clicked.connect(self.switchToRegister)
        self.myHBoxLayout3.insertWidget(0, self.myRegisterButton)
        self.myHBoxLayout3.setAlignment(Qt.AlignCenter)


        #CHECKING LOGIN STATUS LOOP TIMER
        self.myLoopTimer=QTimer()
        self.myLoopTimer.timeout.connect(self.checkLoop)
        self.myLoopTimer.start(1000)


        #WAIT FOR GAME TIMER
        self.myWaitForGameTimer=QTimer()
        self.myWaitForGameTimer.timeout.connect(self.waitForMainGameLoop)


    def switchToRegister(self):
        self.toggleOff()
        self.myRegisterScreen.toggleOn()
        pass

    def switchToLogin(self):
        self.toggleOff()
        self.myLoginScreen.toggleOn()
        pass

    def toggleOn(self):
        self.show()

    def toggleOff(self):
        self.hide()

    def checkLoop(self):
        if self.myLoginScreen.getLoginStatus():
            self.authDone=True
            self.myLoginScreen.toggleOff()
            self.myUsername=self.myLoginScreen.getUsername()
        if self.myRegisterScreen.getRegisterStatus():
            self.authDone=True
            self.myRegisterScreen.toggleOff()
            self.myUsername=self.myRegisterScreen.getUsername()

        if self.authDone:
            self.LOGIN_QUEUE.put(f"LOGIN.{self.myUsername}")
            self.toggleOff()
            self.myWaitingForPlayersScreen.toggleOn()
            self.myLoopTimer.stop()
            self.myWaitForGameTimer.start(100)


    def waitForMainGameLoop(self):
        nrOfLoggedPlayers = self.MAIN_GAME.getEngine().getNrOfLoggedPlayers()
        self.myWaitingForPlayersScreen.updateText(str(nrOfLoggedPlayers))
        if nrOfLoggedPlayers == 2:
            self.myWaitingForPlayersScreen.toggleOff()
            self.MAIN_GAME.toggleOn()
            self.MAIN_GAME.myUsername=self.myUsername

    def getAuthStatus(self):
        return self.authDone

