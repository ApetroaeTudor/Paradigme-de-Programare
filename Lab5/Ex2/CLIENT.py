import sys
from multiprocessing.managers import BaseManager
from PyQt5.QtCore import QTimer





from multiprocessing import Process,Queue
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

import interface


# class personalID:
#     playerNr=-1
#     def __init__(self):
#         pass
#
#     def checkQueueForID(self,q:Queue):
#         while self.playerNr==-1:
#             print("HEY")
#             try:
#                 msg=q.get_nowait()
#                 print(msg)
#                 if str(msg).split(".")[0]=="ASSIGN_PLAYER":
#                     self.playerNr=str(msg).split(".")[1]
#             except:
#                 pass
#             time.sleep(0.5)
#         self.myTimer.stop()
#         print(self.playerNr)
#
#     def startPlayerNrAssign(self,q:Queue):
#         self.myTimer=QTimer()
#         self.myTimer.timeout.connect(lambda: self.checkQueueForID(q))
#         self.myTimer.start(500)



class GeneralManager(BaseManager):
    pass

if __name__=="__main__":
    GeneralManager.register('get_LoginQueue')
    GeneralManager.register('get_GameEngine')
    GeneralManager.register('get_MovesQueue')

    myGeneralManager=GeneralManager(address=('localhost',50000),authkey=b'123')
    myGeneralManager.connect()


    LOGIN_QUEUE:Queue=myGeneralManager.get_LoginQueue()
    GAME_ENGINE=myGeneralManager.get_GameEngine()
    MOVES_QUEUE=myGeneralManager.get_MovesQueue()




    LOGIN_QUEUE.put("LOGIN.HEY")
    print("msg sent")

    clientApp=QApplication(sys.argv)
    clientWindow=interface.GameInterface(GAME_ENGINE,LOGIN_QUEUE,MOVES_QUEUE)
    clientWindow.show()
    clientApp.exec()




    # linkToServerGameEngine=myGeneralManager.get_GameEngine()