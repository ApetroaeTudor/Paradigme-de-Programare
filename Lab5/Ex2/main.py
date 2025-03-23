import sys
from PyQt5.QtWidgets import QApplication
import gameEngine as gm
import interface as i

from multiprocessing import Process, Queue

if __name__=="__main__":

    loginQueue=Queue()
    movesQueue=Queue()
    loggedUsersQueue=Queue()

    myApp=QApplication(sys.argv)
    myGame=gm.MyGame()
    myMainWindow= i.GameInterface(myGame,loginQueue,movesQueue,loggedUsersQueue)
    myMainWindow.show()
    myApp.exec()