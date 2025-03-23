from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QMainWindow
from PyQt5.QtCore import QSize
import constants as c
import interface as i
import msgQueue as mq

def setLabelWithText(myLabel:QLabel,myText:str):
    myLabel.setText(myText)
    myLabel.update()

def disableButtons(myBtnList:list[QPushButton]):
    for btn in myBtnList:
        btn.setEnabled(False)
        btn.update()

def enableButtons(myBtnList:list[QPushButton]):
    for btn in myBtnList:
        btn.setEnabled(True)
        btn.update()


def disableButtonMatrix(myBtnMatrx:list[list[QPushButton]]):
    for elem in myBtnMatrx:
        disableButtons(elem)

def enableButtonMatrix(myBtnMatrix:list[list[QPushButton]]):
    for elem in myBtnMatrix:
        enableButtons(elem)



def initButtonsForGame(myParentLabel:QLabel,currentState,root:QMainWindow)->list:
    firstRow=[]
    secondRow=[]
    thirdRow=[]

    hBoxLayout1=QHBoxLayout(); hBoxLayout2=QHBoxLayout(); hBoxLayout3=QHBoxLayout()
    vBoxLayout=QVBoxLayout(); vBoxLayout.insertItem(0,hBoxLayout1); vBoxLayout.insertItem(1,hBoxLayout2); vBoxLayout.insertItem(2,hBoxLayout3)

    btn00=i.GameButton("00",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout1.insertWidget(0,btn00)
    btn00.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("MOVE.00"+"."+root.playerNr,root.movesQueue)).start())
    btn00.setStyleSheet("color: white")
    btn00.setFont(QFont("Helvetica",80))
    firstRow.append(btn00)

    btn01=i.GameButton("01",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout1.insertWidget(1,btn01)
    btn01.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("MOVE.01"+"."+root.playerNr,root.movesQueue)).start())
    btn01.setStyleSheet("color: white")
    btn01.setFont(QFont("Helvetica", 80))
    firstRow.append(btn01)

    btn02=i.GameButton("02",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout1.insertWidget(2,btn02)
    btn02.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("MOVE.02"+"."+root.playerNr,root.movesQueue)).start())
    btn02.setStyleSheet("color: white")
    btn02.setFont(QFont("Helvetica", 80))
    firstRow.append(btn02)



    btn10=i.GameButton("10",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout2.insertWidget(0,btn10)
    btn10.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("MOVE.10"+"."+root.playerNr,root.movesQueue)).start())
    btn10.setStyleSheet("color: white")
    btn10.setFont(QFont("Helvetica", 80))
    secondRow.append(btn10)

    btn11=i.GameButton("11",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout2.insertWidget(1,btn11)
    btn11.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("MOVE.11"+"."+root.playerNr,root.movesQueue)).start())
    btn11.setStyleSheet("color: white")
    btn11.setFont(QFont("Helvetica", 80))
    secondRow.append(btn11)

    btn12=i.GameButton("12",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout2.insertWidget(2,btn12)
    btn12.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("MOVE.12"+"."+root.playerNr,root.movesQueue)).start())
    btn12.setStyleSheet("color: white")
    btn12.setFont(QFont("Helvetica", 80))
    secondRow.append(btn12)




    btn20=i.GameButton("20",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout3.insertWidget(0,btn20)
    btn20.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("MOVE.20"+"."+root.playerNr,root.movesQueue)).start())
    btn20.setStyleSheet("color: white")
    btn20.setFont(QFont("Helvetica", 80))
    thirdRow.append(btn20)

    btn21=i.GameButton("21",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout3.insertWidget(1,btn21)
    btn21.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("MOVE.21"+"."+root.playerNr,root.movesQueue)).start())
    btn21.setStyleSheet("color: white")
    btn21.setFont(QFont("Helvetica", 80))
    thirdRow.append(btn21)

    btn22=i.GameButton("22",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout3.insertWidget(2,btn22)
    btn22.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("MOVE.22"+"."+root.playerNr,root.movesQueue)).start())
    btn22.setStyleSheet("color: white")
    btn22.setFont(QFont("Helvetica", 80))
    thirdRow.append(btn22)


    if myParentLabel.layout() is None:
        myParentLabel.setLayout(vBoxLayout)


    finalList=[]; finalList.append(firstRow); finalList.append(secondRow); finalList.append(thirdRow)
    # disableButtonMatrix(finalList)
    return finalList

def deleteButtonsForGame(myParentLabel:QLabel):
    for child in myParentLabel.children():
        child.deleteLater()
    