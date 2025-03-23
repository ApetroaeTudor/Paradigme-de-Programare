from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QTextEdit, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer, QSize, Qt
import sys
import DB_Manager as dbm

from multiprocessing import Process, Queue


class WaitingForPlayersWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.myMainWidget = QWidget()
        self.myMainWidget.setFixedSize(QSize(400, 400))
        self.myMainWidget.setStyleSheet("background-color: #2e2e2e")
        self.myMainWidget.setParent(self)
        self.setCentralWidget(self.myMainWidget)

        # TITLE LABEL
        self.myTitleLabel = QLabel()
        self.myTitleLabel.setFixedSize(QSize(350, 100))
        self.myTitleLabel.setStyleSheet("color: white ")
        self.myTitleLabel.setFont(QFont("Helvetica", 30))
        self.myTitleLabel.setText("Waiting for players..")

        # NR OF PLAYERS LABEL
        self.myShowNrOfPlayersLabel = QLabel()
        self.myShowNrOfPlayersLabel.setFixedSize(QSize(300, 200))
        self.myShowNrOfPlayersLabel.setParent(self.myMainWidget)
        self.myShowNrOfPlayersLabel.setStyleSheet("background-color : rgba(255, 0, 0, 0.2); color: white ")

        self.myHBoxLayout1 = QHBoxLayout()
        self.myHBoxLayout2 = QHBoxLayout()
        self.myVBoxLayout = QVBoxLayout()

        self.myHBoxLayout1.insertWidget(0, self.myShowNrOfPlayersLabel)
        self.myHBoxLayout2.insertWidget(0, self.myTitleLabel)
        self.myHBoxLayout2.setAlignment(Qt.AlignCenter)

        self.myVBoxLayout.insertLayout(0, self.myHBoxLayout2)
        self.myVBoxLayout.insertLayout(1, self.myHBoxLayout1)
        self.myVBoxLayout.insertStretch(2)

        self.myMainWidget.setLayout(self.myVBoxLayout)

    def toggleOn(self):
        self.show()

    def toggleOff(self):
        self.hide()

    def updateText(self, nrOfPlayers: str):
        self.myShowNrOfPlayersLabel.setText(f"{nrOfPlayers}/2")
        self.update()


