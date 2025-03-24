from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QTextEdit, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer, QSize, Qt
import sys
import DB_Manager as dbm
from multiprocessing import Process,Queue

import re


class RegisterScreen(QMainWindow):
    registerDone:bool

    def __init__(self,DBM:dbm.DatabaseManager,ERQ:Queue,LOGGED_USERS_QUEUE:Queue):
        super().__init__()

        self.registerDone=False
        self.myDBManager = DBM
        self.ERROR_QUEUE=ERQ

        self.myUsername=""


        # MAIN SETUP
        self.setWindowTitle("Register"); self.myMainWidget = QWidget(); self.myMainWidget.setFixedSize(400, 500); self.setCentralWidget(self.myMainWidget); self.myMainWidget.setStyleSheet("background-color: #2e2e2e ")
        self.setMaximumSize(400,500)
        # HBOXES
        self.myHBoxLayout1 = QHBoxLayout();self.myHBoxLayout2 = QHBoxLayout();self.myHBoxLayout3 = QHBoxLayout();self.myHBoxLayout4 = QHBoxLayout();self.myHBoxLayout5 = QHBoxLayout()

        # MAIN VBOXLAYOUT
        self.myVBoxMainLayout = QVBoxLayout()
        self.myVBoxMainLayout.insertSpacing(0, 20)
        self.myVBoxMainLayout.insertLayout(1, self.myHBoxLayout1) #titlu
        self.myVBoxMainLayout.insertSpacing(2, 100)

        self.myVBoxMainLayout.insertLayout(3, self.myHBoxLayout2) #email box
        self.myVBoxMainLayout.insertSpacing(4, 25)
        self.myVBoxMainLayout.insertLayout(5, self.myHBoxLayout3) #user box
        self.myVBoxMainLayout.insertSpacing(6, 25)

        self.myVBoxMainLayout.insertLayout(7, self.myHBoxLayout4) #pass box
        self.myVBoxMainLayout.insertSpacing(8, 25)

        self.myVBoxMainLayout.insertLayout(9, self.myHBoxLayout5) #register Button
        self.myVBoxMainLayout.insertStretch(10)

        self.myMainWidget.setLayout(self.myVBoxMainLayout)

        # TITLE LABEL
        self.myTitleLabel = QLabel(); self.myTitleLabel.setText("REGISTER"); self.myTitleLabel.setFont(QFont("Helvetica", 23, QFont.Bold))
        self.myTitleLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white; border-radius: 5px; ")
        self.myHBoxLayout1.insertWidget(0, self.myTitleLabel)
        self.myHBoxLayout1.setAlignment(Qt.AlignCenter)

        #EMAIL FIELD
        self.myEmailLabel=QLabel(); self.myEmailLabel.setText("Email:"); self.myTitleLabel.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.myEmailLabel.setAlignment(Qt.AlignCenter)
        self.myEmailLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white; border-radius: 5px; ")
        self.myEmailLabel.setFixedSize(QSize(60,30))

        self.myEmailTextField=QTextEdit(); self.myEmailTextField.setFixedSize(QSize(120,30))
        self.myEmailTextField.setStyleSheet("color: white")
        self.myHBoxLayout2.insertWidget(0,self.myEmailLabel)
        self.myHBoxLayout2.insertSpacing(1,20)
        self.myHBoxLayout2.insertWidget(2,self.myEmailTextField)
        self.myHBoxLayout2.setAlignment(Qt.AlignCenter)

        # USER FIELD
        self.myUserLabel = QLabel()
        self.myUserLabel.setText("User:")
        self.myUserLabel.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.myUserLabel.setAlignment(Qt.AlignCenter)
        self.myUserLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white; border-radius: 5px; ")
        self.myUserLabel.setFixedSize(QSize(60, 30))

        self.myUserTextField = QTextEdit()
        self.myUserTextField.setStyleSheet("color: white")
        self.myUserTextField.setFixedSize(QSize(120, 30))
        self.myHBoxLayout3.insertWidget(0, self.myUserLabel)
        self.myHBoxLayout3.insertSpacing(1, 20)
        self.myHBoxLayout3.insertWidget(2, self.myUserTextField)
        self.myHBoxLayout3.setAlignment(Qt.AlignCenter)

        # PASSWORD FIELD
        self.myPasswordLabel = QLabel()
        self.myPasswordLabel.setText("Pass:")
        self.myPasswordLabel.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.myPasswordLabel.setAlignment(Qt.AlignCenter)
        self.myPasswordLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white; border-radius: 5px; ")
        self.myPasswordLabel.setFixedSize(QSize(60, 30))

        self.myPasswordTextField = QTextEdit()
        self.myPasswordTextField.setStyleSheet("color: white")
        self.myPasswordTextField.setFixedSize(QSize(120, 30))
        self.myHBoxLayout4.insertWidget(0, self.myPasswordLabel)
        self.myHBoxLayout4.insertSpacing(1, 20)
        self.myHBoxLayout4.insertWidget(2, self.myPasswordTextField)
        self.myHBoxLayout4.setAlignment(Qt.AlignCenter)


        # REGISTER BUTTON
        self.myRegisterButton = QPushButton(); self.myRegisterButton.setText("REGISTER"); self.myRegisterButton.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white ")
        self.myRegisterButton.setFixedSize(QSize(200, 60))
        self.myHBoxLayout5.insertWidget(0, self.myRegisterButton)
        self.myHBoxLayout5.setAlignment(Qt.AlignCenter)
        self.myRegisterButton.clicked.connect(self.attemptRegister_TiedToRegisterBtn)

        #ERROR LABEL
        self.myErrorLabel = QLabel()
        self.myErrorLabel.setFixedSize(QSize(120, 30))
        self.myErrorLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white; border-radius: 5px; ")
        self.myErrorLabel.setParent(self.myMainWidget)
        self.myErrorLabel.setAlignment(Qt.AlignCenter)
        self.myErrorLabel.move(140, 455)
        self.myErrorLabel.hide()

        #ERROR TIMER
        self.myErrorTimer=QTimer()

        #LOOP TIMER
        self.myLoopTimer=QTimer()
        self.myLoopTimer.timeout.connect(self.checkErrorQueue)
        self.myLoopTimer.start(200)

    def attemptRegister_TiedToRegisterBtn(self):
        myInput_Email = self.myEmailTextField.toPlainText()
        if not myInput_Email or myInput_Email.isspace(): #or not re.fullmatch(myInput_Email,r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+$"):
            self.setErrorLabel("No Email", self.myErrorTimer)
            return
        myInput_Username=self.myUserTextField.toPlainText()
        if not myInput_Username or myInput_Username.isspace():
            self.setErrorLabel("No Username",self.myErrorTimer)
            return
        myInput_Password=self.myPasswordTextField.toPlainText()
        if not myInput_Password or myInput_Password.isspace():
            self.setErrorLabel("No Pass",self.myErrorTimer)
            return

        try:
            self.myDBManager.insertAuthenticationEntry(myInput_Email,myInput_Username,myInput_Password)
            self.registerDone=True
            self.myUsername=myInput_Username
        except:
            pass

    def getRegisterStatus(self):
        return self.registerDone

    def toggleOn(self):
        self.show()

    def toggleOff(self):
        self.hide()

    def checkErrorQueue(self):
        try:
            msg=self.ERROR_QUEUE.get_nowait()
            if str(msg).split(".")[0]=="DB_ERROR":
                if str(msg).split(".")[1]=="COULD_NOT_INSERT_AUTHENTICATION_ENTRY":
                    self.setErrorLabel("UserExists",self.myErrorTimer)
            else:
                self.ERROR_QUEUE.put(msg)
        except:
            pass

    def setErrorLabel(self,errorMsg:str,errorTimer:QTimer):
        self.myErrorLabel.setText(errorMsg)
        self.myErrorLabel.show()
        errorTimer.timeout.connect(lambda:self.myErrorLabel.hide())
        errorTimer.start(500)

    def getUsername(self):
        return self.myUsername