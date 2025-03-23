from PyQt5.QtWidgets import QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QMainWindow
from PyQt5.QtCore import QSize
import constants as c
import interface as i
import msgQueue as mq


def initButtonsForGame(myParentLabel:QLabel,currentState,root:QMainWindow)->list:
    firstRow=[]
    secondRow=[]
    thirdRow=[]

    hBoxLayout1=QHBoxLayout(); hBoxLayout2=QHBoxLayout(); hBoxLayout3=QHBoxLayout()
    vBoxLayout=QVBoxLayout(); vBoxLayout.insertItem(0,hBoxLayout1); vBoxLayout.insertItem(1,hBoxLayout2); vBoxLayout.insertItem(2,hBoxLayout3)

    btn00=i.GameButton("00",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout1.insertWidget(0,btn00)
    btn00.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("00",mq.asyncQueue)).start())
    firstRow.append(btn00)

    btn01=i.GameButton("01",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout1.insertWidget(1,btn01)
    btn01.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("01",mq.asyncQueue)).start())
    firstRow.append(btn01)

    btn02=i.GameButton("02",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout1.insertWidget(2,btn02)
    btn02.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("02",mq.asyncQueue)).start())
    firstRow.append(btn02)



    btn10=i.GameButton("10",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout2.insertWidget(0,btn10)
    btn10.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("10",mq.asyncQueue)).start())
    secondRow.append(btn10)

    btn11=i.GameButton("11",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout2.insertWidget(1,btn11)
    btn11.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("11",mq.asyncQueue)).start())
    secondRow.append(btn11)

    btn12=i.GameButton("12",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout2.insertWidget(2,btn12)
    btn12.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("12",mq.asyncQueue)).start())
    secondRow.append(btn12)




    btn20=i.GameButton("20",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout3.insertWidget(0,btn20)
    btn20.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("20",mq.asyncQueue)).start())
    thirdRow.append(btn20)

    btn21=i.GameButton("21",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout3.insertWidget(1,btn21)
    btn21.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("21",mq.asyncQueue)).start())
    thirdRow.append(btn21)

    btn22=i.GameButton("22",c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT,myParentLabel,root);hBoxLayout3.insertWidget(2,btn22)
    btn22.clicked.connect(lambda:mq.Process(mq.putMsgToQueue("22",mq.asyncQueue)).start())
    thirdRow.append(btn22)


    if myParentLabel.layout() is None:
        myParentLabel.setLayout(vBoxLayout)
    finalList=[]; finalList.append(firstRow); finalList.append(secondRow); finalList.append(thirdRow)
    return finalList

def deleteButtonsForGame(myParentLabel:QLabel):
    for child in myParentLabel.children():
        child.deleteLater()
    