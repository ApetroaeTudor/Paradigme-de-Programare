import os
import sys
from multiprocessing import Process,Queue
from tkinter.constants import CENTER

from PyQt5.QtCore import QRect, QTimeZone, lowercasebase
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QHBoxLayout, QPushButton, QVBoxLayout, QTextEdit, QWidget, QMainWindow, QApplication
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QTimer
import Dimensions as dim
import FileIO as fio

from pathlib import Path
import time

import subprocess

def pushMessageToAsyncQueue(q:Queue,msg:str):
    q.put(msg)


def moveRightPanel(myRightPanel:QLabel,startPos:QRect,endPos:QRect,showFlag:bool):
    myAni = QPropertyAnimation(myRightPanel, b"geometry")
    myAni.setDuration(100)
    myRightPanel.animation = myAni

    if showFlag==True:
        myAni.setStartValue(startPos)
        myAni.setEndValue(endPos)
        myRightPanel.animation.start()
    else:
        myAni.setStartValue(endPos)
        myAni.setEndValue(startPos)
        myRightPanel.animation.start()

def initButtons(parentWidget:QLabel,nrOfEntries:int):

    allMyEntryNames=fio.getAllEntryNames("TextFiles/Entries")

    myFinalVBoxLayout=QVBoxLayout()
    myTitleLabel=QLabel()
    index=1
    myTitleLabel.setText("ENTRIES:")
    myTitleLabel.setFixedSize(QSize(100,30))
    myFinalVBoxLayout.insertSpacing(0,dim.LARGE_UI_GAP*2)

    myTitleHBoxLayout=QHBoxLayout()
    myTitleHBoxLayout.insertWidget(0,myTitleLabel,1,Qt.AlignCenter)

    myFinalVBoxLayout.insertLayout(index,myTitleHBoxLayout)

    buttonList=[]

    rng=nrOfEntries
    if nrOfEntries>10:
        rng=10

    for i in range(0,rng):
        myHBoxLayout=QHBoxLayout()
        myLabel=QLabel()
        myLabel.setFixedSize(QSize(30,30))
        myLabel.setText(str(i))
        myButton=QPushButton()
        myButton.setFixedSize(QSize(100,30))
        myButton.setText("Load")
        myButton.setParent(parentWidget)
        buttonList.append(myButton)

        myEntryTitle=allMyEntryNames.pop(0)
        myEntryTitleLabel=QLabel()
        myEntryTitleLabel.setFixedSize(QSize(200,30))
        myEntryTitleLabel.setText(myEntryTitle)



        myHBoxLayout.insertSpacing(0,dim.LARGE_UI_GAP)
        myHBoxLayout.insertWidget(1,myLabel)
        myHBoxLayout.insertWidget(2,myButton)
        myHBoxLayout.insertWidget(3,myEntryTitleLabel)
        myHBoxLayout.insertStretch(4)
        index=index+2
        myFinalVBoxLayout.insertSpacing(index-1,dim.SMALL_UI_GAP)
        myFinalVBoxLayout.insertLayout(index,myHBoxLayout)
    myFinalVBoxLayout.insertStretch(index+1)

    return myFinalVBoxLayout,buttonList



def linkBtnConnectsToEntries(ownerPanel:QMainWindow,btnList:list[QPushButton],myTextEdit:QTextEdit,myTitleTextEdit:QTextEdit,fileTitles:list[str]):
    def loadFileContent(fileTitle: str):
        content = fio.readContentFromFile(fileTitle)
        myTextEdit.setText(content)
        myTitleTextEdit.setText(fileTitle)
        myTitleTextEdit.setAlignment(Qt.AlignCenter)
        myTitleTextEdit.setFont(QFont("Helvetica",20,QFont.Bold))

    for btn, currentTitle in zip(btnList, fileTitles):
        btn.setParent(ownerPanel)
        btn.clicked.connect(lambda _, title=currentTitle: loadFileContent(title))


def checkIfAnyButtonHasFocus(btnList:list):
    if any(btn.hasFocus() for btn in btnList):
        return True
    return False


def setErrorLabel(myRootWidget:QWidget,myErrorLabel:QLabel,myErrorText:str,posX:int,posY:int,myTimer:QTimer):
    myErrorLabel.setText(myErrorText)
    myErrorLabel.setAlignment(Qt.AlignCenter)
    myErrorLabel.setFixedSize(QSize(dim.STD_BUTTON_WIDTH, int(dim.STD_BUTTON_HEIGHT / 2)))
    myErrorLabel.setStyleSheet("background-color : red; color : white;")
    myErrorLabel.setParent(myRootWidget)
    myErrorLabel.move(posX,posY)
    myErrorLabel.show()
    myTimer.timeout.connect(lambda: myErrorLabel.hide())
    myTimer.start(1000)

def processDeleteInput(myRootWidget:QWidget,myTitleTextBox:QTextEdit,myErrorLabel:QLabel,myBodyTextBox:QTextEdit, myTimer:QTimer):
    titleText=myTitleTextBox.toPlainText()
    if titleText[0]=='"':
        setErrorLabel(myRootWidget,myErrorLabel,"Nothing to Delete",130,int(dim.WINDOW_HEIGHT*0.95),myTimer)
    else:
        for file in os.listdir("TextFiles/Entries"):
            if titleText==file.title():
                filePath=Path("TextFiles/Entries/"+titleText)
                if filePath.exists():
                    myTitleTextBox.clear()
                    myBodyTextBox.clear()
                    filePath.unlink()
                    subprocess.Popen([sys.executable] + sys.argv)
                    QApplication.exit(0)


def processSaveInput(myRootWidget:QWidget,myTitleTextBox:QTextEdit,myErrorLabel:QLabel,myBodyTextBox:QTextEdit, myTimer:QTimer):
    timestamp=time.time()
    readableTimestamp=time.ctime(timestamp)
    bodyContent=myBodyTextBox.toPlainText()
    if not bodyContent:
        setErrorLabel(myRootWidget,myErrorLabel,"Nothing to Save",130,int(dim.WINDOW_HEIGHT*0.95),myTimer)

    else:
        with open(f"TextFiles/Entries/{readableTimestamp}","w") as file:
            file.write(bodyContent)
            subprocess.Popen([sys.executable] + sys.argv)
            QApplication.exit(0)

def processPlusFromSecondWindow(mySecondaryWindow:QMainWindow,mySecondaryTextbox:QTextEdit,myErrorLabel:QLabel,myTimer:QTimer):
    content=mySecondaryTextbox.toPlainText()
    if not content:
        setErrorLabel(mySecondaryWindow,myErrorLabel,"Nothing To Add",180,360,myTimer)
        return
    if not content[0] or not content[len(content)-1]=='"':
        setErrorLabel(mySecondaryWindow,myErrorLabel,'use quotes',180,360,myTimer)
        return
    fio.writeContentToCitate(content)
    mySecondaryTextbox.clear()
    mySecondaryWindow.hide()
