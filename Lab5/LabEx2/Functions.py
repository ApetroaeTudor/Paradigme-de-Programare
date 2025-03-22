from multiprocessing import Process,Queue

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation
import Dimensions as dim

def pushMessageToAsyncQueue(q:Queue,msg:str):
    q.put(msg)


def moveRightPanel(myRightPanel:QLabel,startPos:QRect,endPos:QRect,showFlag:bool):
    myAni = QPropertyAnimation(myRightPanel, b"geometry")
    myAni.setDuration(100)
    myRightPanel.animation = myAni

    if showFlag==True:
        myRightPanel.setFocus()
        myAni.setStartValue(startPos)
        myAni.setEndValue(endPos)
        myRightPanel.animation.start()
    else:
        myAni.setStartValue(endPos)
        myAni.setEndValue(startPos)
        myRightPanel.animation.start()


