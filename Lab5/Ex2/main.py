import interface
import sys
from PyQt5.QtWidgets import QApplication

if __name__=="__main__":
    myApp=QApplication(sys.argv)
    myMainWindow=interface.GameInterface()
    myMainWindow.show()
    myApp.exec()