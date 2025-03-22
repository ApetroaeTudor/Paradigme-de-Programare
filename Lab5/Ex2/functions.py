from PyQt5.QtWidgets import QPushButton,QLabel,QHBoxLayout,QVBoxLayout,QWidget
from PyQt5.QtCore import QSize
import constants as c

def initButtonsForGame(myParentLabel:QLabel)->list:
    firstRow=[]
    secondRow=[]
    thirdRow=[]

    hBoxLayout1=QHBoxLayout(); hBoxLayout2=QHBoxLayout(); hBoxLayout3=QHBoxLayout()
    vBoxLayout=QVBoxLayout(); vBoxLayout.insertItem(0,hBoxLayout1); vBoxLayout.insertItem(1,hBoxLayout2); vBoxLayout.insertItem(2,hBoxLayout3)

    for i in range(0,9):
        myButton=QPushButton(); myButton.setFixedSize(QSize(c.GAME_BTN_WIDTH,c.GAME_BTN_HEIGHT))
        myButton.setParent(myParentLabel)
        if i < 3:
            hBoxLayout1.insertWidget(i,myButton)
            firstRow.append(myButton)
        elif i<6:
            hBoxLayout2.insertWidget(i-3,myButton)
            secondRow.append(myButton)
        elif i<9:
            hBoxLayout3.insertWidget(i-6,myButton)
            thirdRow.append(myButton)

    if myParentLabel.layout() is None:
        myParentLabel.setLayout(vBoxLayout)
    finalList=[]; finalList.append(firstRow); finalList.append(secondRow); finalList.append(thirdRow)
    return finalList

def deleteButtonsForGame(myParentLabel:QLabel):
    for child in myParentLabel.children():
        child.deleteLater()
    