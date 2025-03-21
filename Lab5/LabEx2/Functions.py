from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation
import multiprocessing as mp


def animateRightPanel(myRightPanel:QLabel,startPos:QRect,endPos:QRect):
    #def executeAsync(myRightPanel:QLabel,startPos:QRect,endPos:QRect):
    myAni=QPropertyAnimation(myRightPanel,b"geometry")
    myAni.setDuration(500)
    myAni.setTargetObject(myRightPanel)

    myAni.setStartValue(startPos)
    myAni.setEndValue(endPos)
    myAni.start()
    print("ani started")

    #myProcess=mp.Process(target=lambda: executeAsync(myRightPanel,startPos,endPos))
    #myProcess.start()