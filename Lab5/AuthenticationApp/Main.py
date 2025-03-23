from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QTextEdit, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer, QSize, Qt
import sys
import DB_Manager as dbm

from multiprocessing import Process,Queue

import WelcomeScreen as ws

if __name__=="__main__":
    myApp=QApplication(sys.argv)

    ERROR_QUEUE=Queue()

    myWelcomeScreen=ws.WelcomeScreen(ERROR_QUEUE)
    myWelcomeScreen.toggleOn()

    myApp.exec()