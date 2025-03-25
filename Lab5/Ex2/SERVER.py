import multiprocessing as mp
import threading
from multiprocessing.managers import BaseManager
import gameEngine as gm
import msgQueue as mq
import time

import DB_Manager as dbm

user1=""
user2=""

SERVER_game_engine = gm.MyGame()

SERVER_error_queue = mp.Queue()
SERVER_score=("InvalidUser",0,"InvalidUser",0)
logInQueue = mp.Queue()
movesQueue = mp.Queue()

SERVER_DB_Manager=dbm.DatabaseManager(SERVER_error_queue)

loggedUsers=[]
loggedUsersQueue = mp.Queue()


class GeneralManager(BaseManager):
    pass


def checkState():
    while True:
        moveList=[]
        while True:
            try:
                move=movesQueue.get_nowait()
                moveList.append(move)
            except:
                break
        # print(moveList)
        # print("EngineTurnSERVER:"+str(SERVER_game_engine.getTurn()))


        for move in moveList:
            movesQueue.put(move)

        print(loggedUsers)
        if len(loggedUsers) == 2:
            user1=str(loggedUsers.pop())
            user2=str(loggedUsers.pop())
            id1 = int(SERVER_DB_Manager.getIDbyName(user1))
            id2 = int(SERVER_DB_Manager.getIDbyName(user2))
            resultFromDB = SERVER_DB_Manager.getScoresByPlayerIDS(id1, id2)
            print(resultFromDB)
            if(resultFromDB==None):
                SERVER_DB_Manager.initGameWithUserIDS(id1,id2)
                SERVER_score=(user1,int(0),user2,int(0))
            else:
                # print(user1)
                # print(user2)
                SERVER_score=(user1,int(resultFromDB[0]),user2,int(resultFromDB[1]))


            logInQueue.put("SCORE."+SERVER_score[0]+":"+str(SERVER_score[1])+"--"+str(SERVER_score[2])+":"+str(SERVER_score[3]))
            logInQueue.put("SCORE."+SERVER_score[0]+":"+str(SERVER_score[1])+"--"+str(SERVER_score[2])+":"+str(SERVER_score[3]))

        try:
            msg=logInQueue.get_nowait()

            if str(msg).split(".")[0]=="WINNER":
                winnerName=str(msg).split(".")[1]
                winnerID=SERVER_DB_Manager.getIDbyName(winnerName)
                if str(winnerName)==str(user1):
                    loserID=SERVER_DB_Manager.getIDbyName(user2)
                else:
                    loserID=SERVER_DB_Manager.getIDbyName(user1)
                if winnerID<loserID:
                    SERVER_DB_Manager.incrementPlayer0Score(winnerID,loserID)
                elif winnerID>loserID:
                    SERVER_DB_Manager.incrementPlayer1Score(loserID,winnerID)

            else:
                logInQueue.put(msg)
        except:
            pass
        time.sleep(0.5)



class LoginManager():
    authenticationStatus=0 #0=0 users connected,1=1 user connected, 2=2 users connected

    def checkLoginQueue(self):
        while True and not self.authenticationStatus==2:
            try:
                msg=logInQueue.get_nowait()
                print(f"received msg:{msg}")
                if str(msg).split(".")[0]=="LOGIN":
                    SERVER_game_engine.incrementNrOfLoggedPlayers()
                    logInQueue.put(f"ASSIGN_PLAYER.{self.authenticationStatus}")
                    loggedUsersQueue.put(str(msg).split(".")[1])
                    loggedUsers.append(str(msg).split(".")[1])
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
    GeneralManager.register('get_GameEngine',callable=lambda: SERVER_game_engine,exposed=['getGameState','checkCurrentState','getTurn','takeMoveFromPlayer','resetBoard','getNrOfLoggedPlayers','incrementNrOfLoggedPlayers','getCurrentScore'])
    GeneralManager.register('get_MovesQueue',callable=lambda: movesQueue)
    GeneralManager.register('get_LoggedUsersQueue',callable=lambda: loggedUsersQueue)

    myThread = threading.Thread(target=checkState, daemon=True)
    myThread.start()


    server=myGeneralManager.get_server()
    server.serve_forever()
