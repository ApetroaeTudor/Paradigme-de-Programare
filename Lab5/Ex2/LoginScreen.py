from queue import Queue

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QTextEdit, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer, QSize, Qt
import sys
import DB_Manager as dbm

from multiprocessing import Process,Queue
from queue import Empty


class LoginScreen(QMainWindow):
    loginDone:bool

    def __init__(self,DBM:dbm.DatabaseManager,ERQ:Queue,LOGGED_USERS_QUEUE:Queue):
        super().__init__()

        self.loginDone=False
        self.myDBManager=DBM
        self.ERROR_QUEUE=ERQ
        self.LOGGED_USERS_QUEUE=LOGGED_USERS_QUEUE
        self.myUsername=""


        # MAIN SETUP
        self.setWindowTitle("LOG-IN"); self.myMainWidget = QWidget(); self.myMainWidget.setFixedSize(400, 500); self.setCentralWidget(self.myMainWidget); self.myMainWidget.setStyleSheet("background-color: #2e2e2e ")

        # HBOXES
        self.myHBoxLayout1 = QHBoxLayout();self.myHBoxLayout2 = QHBoxLayout();self.myHBoxLayout3 = QHBoxLayout();self.myHBoxLayout4 = QHBoxLayout();self.myHBoxLayout5 = QHBoxLayout()

        # MAIN VBOXLAYOUT
        self.myVBoxMainLayout = QVBoxLayout()
        self.myVBoxMainLayout.insertSpacing(0, 20)
        self.myVBoxMainLayout.insertLayout(1, self.myHBoxLayout1) #titlu
        self.myVBoxMainLayout.insertSpacing(2, 100)

        self.myVBoxMainLayout.insertLayout(3, self.myHBoxLayout2) #user box
        self.myVBoxMainLayout.insertSpacing(4, 25)

        self.myVBoxMainLayout.insertLayout(5, self.myHBoxLayout3) #pass box
        self.myVBoxMainLayout.insertSpacing(6, 25)

        self.myVBoxMainLayout.insertLayout(7, self.myHBoxLayout4) #register Button
        self.myVBoxMainLayout.insertStretch(8)

        self.myMainWidget.setLayout(self.myVBoxMainLayout)

        # TITLE LABEL
        self.myTitleLabel = QLabel(); self.myTitleLabel.setText("LOG-IN"); self.myTitleLabel.setFont(QFont("Helvetica", 23, QFont.Bold))
        self.myTitleLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white ")
        self.myHBoxLayout1.insertWidget(0, self.myTitleLabel)
        self.myHBoxLayout1.setAlignment(Qt.AlignCenter)

        # USER FIELD
        self.myUserLabel = QLabel()
        self.myUserLabel.setText("User:")
        self.myUserLabel.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.myUserLabel.setAlignment(Qt.AlignCenter)
        self.myUserLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white ")
        self.myUserLabel.setFixedSize(QSize(60, 30))

        self.myUserTextField = QTextEdit()
        self.myUserTextField.setStyleSheet("color: white")
        self.myUserTextField.setFixedSize(QSize(120, 30))
        self.myHBoxLayout2.insertWidget(0, self.myUserLabel)
        self.myHBoxLayout2.insertSpacing(1, 20)
        self.myHBoxLayout2.insertWidget(2, self.myUserTextField)
        self.myHBoxLayout2.setAlignment(Qt.AlignCenter)

        # PASSWORD FIELD
        self.myPasswordLabel = QLabel()
        self.myPasswordLabel.setText("Pass:")
        self.myPasswordLabel.setFont(QFont("Helvetica", 14, QFont.Bold))
        self.myPasswordLabel.setAlignment(Qt.AlignCenter)
        self.myPasswordLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white ")
        self.myPasswordLabel.setFixedSize(QSize(60, 30))

        self.myPasswordTextField = QTextEdit()
        self.myPasswordTextField.setStyleSheet("color: white")
        self.myPasswordTextField.setFixedSize(QSize(120, 30))
        self.myHBoxLayout3.insertWidget(0, self.myPasswordLabel)
        self.myHBoxLayout3.insertSpacing(1, 20)
        self.myHBoxLayout3.insertWidget(2, self.myPasswordTextField)
        self.myHBoxLayout3.setAlignment(Qt.AlignCenter)


        # LOGIN BUTTON
        self.myLoginButton = QPushButton(); self.myLoginButton.setText("LOG-IN"); self.myLoginButton.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white ")
        self.myLoginButton.setFixedSize(QSize(200, 60))
        self.myHBoxLayout4.insertWidget(0, self.myLoginButton)
        self.myLoginButton.clicked.connect(self.attemptLogin_TiedToLoginBtn)
        self.myHBoxLayout4.setAlignment(Qt.AlignCenter)


        # ERROR LABEL
        self.myErrorLabel=QLabel(); self.myErrorLabel.setFixedSize(QSize(120, 30)); self.myErrorLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white ")
        self.myErrorLabel.setParent(self.myMainWidget)
        self.myErrorLabel.setAlignment(Qt.AlignCenter)
        self.myErrorLabel.move(140,440)
        self.myErrorLabel.hide()

        # ERROR TIMER
        self.myErrorTimer = QTimer()

        # LOOP TIMER
        self.myLoopTimer = QTimer()


    def attemptLogin_TiedToLoginBtn(self):
        myInput_Username=self.myUserTextField.toPlainText()
        if not myInput_Username:
            self.setErrorLabel("No User", self.myErrorTimer)
            return
        myInput_Password = self.myPasswordTextField.toPlainText()
        if not myInput_Password:
            self.setErrorLabel("No Pass", self.myErrorTimer)
            return

        try:
            username=self.myDBManager.getUsernameByPassword(str(myInput_Password))
            if str(username)==myInput_Username and not self.checkIfIsLoggedInAlready(myInput_Username):
                self.loginDone=True
                self.myUsername = myInput_Username
        except:
            self.setErrorLabel("InvalidData",self.myErrorTimer)

    def checkIfIsLoggedInAlready(self, input_User: str):
        temp_list = []
        user_found = False

        while True:
            try:
                user = self.LOGGED_USERS_QUEUE.get_nowait()
                temp_list.append(user)
                if input_User == str(user):
                    user_found = True
            except Empty:
                break

        for user in temp_list:
            self.LOGGED_USERS_QUEUE.put(user)

        if user_found:
            raise Exception("User Logged")

        return False

    def getLoginStatus(self):
        return self.loginDone

    def toggleOn(self):
        self.show()

    def toggleOff(self):
        self.hide()

    def setErrorLabel(self, errorMsg: str, errorTimer: QTimer):
        self.myErrorLabel.setText(errorMsg)
        self.myErrorLabel.show()
        errorTimer.timeout.connect(lambda: self.myErrorLabel.hide())
        errorTimer.start(500)


    def checkErrorQueue(self):
        try:
            msg=self.ERROR_QUEUE.get_nowait()
            if str(msg).split(".")[0]=="DB_ERROR":
                if str(msg).split(".")[1]=="USER_NOT_FOUND":
                    self.setErrorLabel("InvalidData",self.myErrorTimer)
            else:
                self.ERROR_QUEUE.put(msg)
        except:
            pass

    def getUsername(self):
        return self.myUsername