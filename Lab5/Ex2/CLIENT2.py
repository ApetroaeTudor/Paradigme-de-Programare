import sys
from multiprocessing.managers import BaseManager
from PyQt5.QtCore import QTimer

from multiprocessing import Process,Queue
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

import interface

import WelcomeScreen as ws



class GeneralManager(BaseManager):
    pass

if __name__=="__main__":
    GeneralManager.register('get_LoginQueue')
    GeneralManager.register('get_GameEngine')
    GeneralManager.register('get_MovesQueue')
    GeneralManager.register('get_LoggedUsersQueue')

    myGeneralManager=GeneralManager(address=('localhost',50000),authkey=b'123')
    myGeneralManager.connect()


    LOGIN_QUEUE:Queue=myGeneralManager.get_LoginQueue()
    GAME_ENGINE=myGeneralManager.get_GameEngine()
    MOVES_QUEUE=myGeneralManager.get_MovesQueue()
    LOGGED_USERS_QUEUE=myGeneralManager.get_LoggedUsersQueue()


    #Error queue for auth in main pentru ca nu imi trebuie nicaieri in server
    ERROR_QUEUE=Queue()


    clientApp=QApplication(sys.argv)
    gameInterface=interface.GameInterface(GAME_ENGINE,LOGIN_QUEUE,MOVES_QUEUE,LOGGED_USERS_QUEUE)
    clientWindow=ws.WelcomeScreen(ERROR_QUEUE,LOGIN_QUEUE,LOGGED_USERS_QUEUE,gameInterface)
    clientWindow.show()
    clientApp.exec()

