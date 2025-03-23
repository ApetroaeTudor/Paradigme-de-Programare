import sys
from PyQt5.QtWidgets import QApplication
import gameEngine as gm
import interface as i

if __name__=="__main__":
    myApp=QApplication(sys.argv)
    myGame=gm.MyGame()
    myMainWindow= i.GameInterface(myGame,0)
    myMainWindow.show()
    myApp.exec()