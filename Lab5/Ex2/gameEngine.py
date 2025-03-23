from multiprocessing import Process, Queue
import msgQueue as mq

class MyGame:
    currentState=[["-","-","-"],
                  ["-","-","-"],
                  ["-","-","-"]]
    turn=0 #turn0 e player1=X, turn1 e player2=O

    def __init__(self):
        pass

    def resetBoard(self):
        self.currentState=[["-","-","-"],
                  ["-","-","-"],
                  ["-","-","-"]]
        self.turn=0


    def validateMove(self,row:int,column:int)->bool:
        if column < 0 or column >2 or row <0 or row >2:
            return False
        if self.currentState[row][column]=='X' or self.currentState[row][column]=='O':
            return False

        return True
    
    def takeMoveFromPlayer(self,row:int,column:int):
        if self.validateMove(row,column):
            if self.turn==0:
                self.currentState[row][column]='X'
            elif self.turn==1:
                self.currentState[row][column]='O'
            self.turn=(self.turn+1)%2

    def checkCurrentState(self)->list: #list[0] e game state(0=finished,1=stillGoing), list[1] e winner-ul(0=X,1=O,2=tie,3=no one yet)
        emptySquares=0
        returnList=[-1,-1]
        for i in range(0,3):
            for j in range(0,3):
                if self.currentState[i][j]=='-':
                    emptySquares+=1
        if emptySquares == 0:
            returnList[0]=0
            returnList[1]=2
            return returnList

        #row checking
        for i in range(0,3):
            isXWinner=True
            isYWinner=True
            for j in range(0,3):
                if self.currentState[i][j]=='O' or self.currentState[i][j]=='-':
                    isXWinner=False
                if self.currentState[i][j]=='X' or self.currentState[i][j]=='-':
                    isYWinner=False
            if isXWinner:
                returnList[0]=0
                returnList[1]=0
                return returnList
            if isYWinner:
                returnList[0]=0
                returnList[1]=1
                return returnList
        
        #column checking
        for j in range(0,3):
            isXWinner=True
            isYWinner=True
            for i in range(0,3):
                if self.currentState[i][j]=='O' or self.currentState[i][j]=='-':
                    isXWinner=False
                if self.currentState[i][j]=='X' or self.currentState[i][j]=='-':
                    isYWinner=False
            if isXWinner:
                returnList[0]=0
                returnList[1]=0
                return returnList
            if isYWinner:
                returnList[0]=0
                returnList[1]=1
                return returnList
            
        #diagonal checking
        if self.currentState[0][0]=='X' and self.currentState[1][1]=='X' and self.currentState[2][2]=='X':
            returnList[0]=0
            returnList[1]=0
            return returnList
        if self.currentState[0][2]=='X' and self.currentState[1][1]=='X' and self.currentState[2][0]=='X':
            returnList[0]=0
            returnList[1]=0
            return returnList


        if self.currentState[0][0]=='O' and self.currentState[1][1]=='O' and self.currentState[2][2]=='O':
            returnList[0]=0
            returnList[1]=1
            return returnList
        if self.currentState[0][2]=='O' and self.currentState[1][1]=='O' and self.currentState[2][0]=='O':
            returnList[0]=0
            returnList[1]=1
            return returnList
        
        returnList[0]=1
        returnList[1]=3

        return returnList
    
    def printBoard(self):
        for elem in self.currentState:
            print(elem)
        print("\n")

#     def gameLoop(self):
#         activeState=self.checkCurrentState()
#         while activeState[0]==1:
#             self.printBoard()
#             while True:
#                 try:
#                     move=mq.asyncQueue.get_nowait()
#                     row=int(str(move)[0])
#                     col=int(str(move)[1])
#                     if self.validateMove(row, col):
#                         break
#                 except:
#                     pass
#             self.takeMoveFromPlayer(row,col)
#             activeState=self.checkCurrentState()
#
#         self.printBoard()
#         if activeState[1]==0:
#             print("X wins")
#         elif activeState[1]==1:
#             print("0 wins")
#         elif activeState[1]==2:
#             print("tie")
#
#
# myXOgame=MyGame()