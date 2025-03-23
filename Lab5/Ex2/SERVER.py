import multiprocessing as mp
import threading
from multiprocessing.managers import BaseManager
import gameEngine as gm
import msgQueue as mq
import time

SERVER_game_engine = gm.MyGame()
logInQueue = mp.Queue()
movesQueue = mp.Queue()


class GeneralManager(BaseManager):
    pass


class LoginManager():
    authenticationStatus=0 #0=0 users connected,1=1 user connected, 2=2 users connected

    def checkLoginQueue(self):
        while True and not self.authenticationStatus==2:
            try:
                msg=logInQueue.get_nowait()
                print(f"received msg:{msg}")
                if str(msg).split(".")[0]=="LOGIN":
                    logInQueue.put(f"ASSIGN_PLAYER.{self.authenticationStatus}")
                    self.authenticationStatus+=1
                else:
                    logInQueue.put(msg)
            except:
                pass
            time.sleep(0.5)
        print("authentication Done")



    def startLoginSession(self):
        myThread=threading.Thread(target=self.checkLoginQueue,daemon=True)
        myThread.start()



if __name__=="__main__":
    myLoginManager=LoginManager()
    myLoginManager.startLoginSession()

    myGeneralManager=GeneralManager(address=('localhost',50000),authkey=b'123')

    GeneralManager.register('get_LoginQueue',callable=lambda: logInQueue)
    GeneralManager.register('get_GameEngine',callable=lambda: SERVER_game_engine,exposed=['getGameState','checkCurrentState','getTurn','takeMoveFromPlayer','resetBoard'])
    GeneralManager.register('get_MovesQueue',callable=lambda: movesQueue)

    server=myGeneralManager.get_server()
    server.serve_forever()
