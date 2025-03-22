import Dimensions
from multiprocessing import Process,Queue

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, \
    QLineEdit, QTextEdit
from PyQt5.QtCore import Qt, QSize, QPropertyAnimation, QRect, QPoint, QTimer, QEvent

import Dimensions as dim
import Functions as fn
import FileIO as fio

import sys



class MainWindow(QMainWindow):
    myMainWidget:QLabel
    myTitleLabel:QLabel
    myLeftVBoxLayout:QVBoxLayout
    myLeftHBoxLayout1:QHBoxLayout
    myLeftHBoxLayout2:QHBoxLayout
    myLoadButton:QPushButton
    mySaveButton:QPushButton

    myRightVBoxLayout:QVBoxLayout

    myTitleTextbox:QTextEdit
    myBodyTextbox:QTextEdit

    myBridgeHBoxLayout:QHBoxLayout
    myRightPanel:QLabel
    rightPanelDocked:QRect
    rightPanelVisible:QRect

    myNoEntriesLabel:QLabel

    showFlag=False


    myTimer:QTimer

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(dim.WINDOW_WIDTH,dim.WINDOW_HEIGHT))
        self.setWindowTitle("MyJournal")

        #BUTTONS
        self.myLoadButton=QPushButton("Load")
        self.myLoadButton.setFixedSize(QSize(dim.STD_BUTTON_WIDTH,dim.STD_BUTTON_HEIGHT))

        self.myLoadButton.clicked.connect(lambda: Process(fn.pushMessageToAsyncQueue(dim.asyncQueue,"summonRightPanel")).start())

        self.mySaveButton=QPushButton("Save")
        self.mySaveButton.setFixedSize(QSize(dim.STD_BUTTON_WIDTH,dim.STD_BUTTON_HEIGHT))

        #TITLE TEXTBOX
        self.myTitleTextbox=QTextEdit()
        self.myTitleTextbox.setFixedSize(QSize(self.myLoadButton.size().width()*2+dim.LARGE_UI_GAP,dim.TITLE_BOX_HEIGHT))
        self.myTitleTextbox.setFont(QFont("Helvetica",10))
        self.myTitleTextbox.setReadOnly(True)
        self.myTitleTextbox.setText(fio.getRandomLineFromFile("TextFiles/Citate.txt"))

        #BODY TEXTBOX
        self.myBodyTextbox=QTextEdit()
        self.myBodyTextbox.setFixedSize(QSize(self.myTitleTextbox.size().width(),dim.BODY_TEXTBOX_HEIGHT))


        #SET IMAGE
        self.myMainWidget=QLabel()
        self.myMainWidget.setPixmap(QPixmap("res/w95.jpeg"))
        self.myMainWidget.setScaledContents(True)


        #TEXT LABELS
        self.myTitleLabel=QLabel()
        self.myTitleLabel.setText("myJournal")

        #HBOX FOR TITLE
        self.myLeftHBoxLayout1=QHBoxLayout()
        self.myLeftHBoxLayout1.insertWidget(0,self.myTitleLabel)
        self.myLeftHBoxLayout1.insertStretch(1)

        #HBOX FOR LOAD/SAVE
        self.myLeftHBoxLayout2=QHBoxLayout()
        self.myLeftHBoxLayout2.insertWidget(0,self.myLoadButton)
        self.myLeftHBoxLayout2.insertSpacing(1,dim.LARGE_UI_GAP)
        self.myLeftHBoxLayout2.insertWidget(2,self.mySaveButton)
        self.myLeftHBoxLayout2.insertStretch(3)


        #RIGHT PANEL
        self.myRightPanel=QLabel()
        self.myRightPanel.setFixedSize(QSize(dim.RIGHT_PANEL_WIDTH,dim.RIGHT_PANEL_HEIGHT))
        self.myRightPanel.setPixmap(QPixmap("res/RightPanel.png"))
        self.myRightPanel.setScaledContents(True)
        self.myRightPanel.setParent(self.myMainWidget)
        self.myRightPanel.move(dim.WINDOW_WIDTH,0)
        self.rightPanelDocked = self.myRightPanel.geometry()
        self.rightPanelVisible = QRect(self.myRightPanel.geometry().x() - dim.RIGHT_PANEL_WIDTH, self.myRightPanel.geometry().y(), self.myRightPanel.width(), self.myRightPanel.height())
        self.isRightPanelVisible=[]
        QApplication.instance().installEventFilter(self)


        #RIGHT PANEL CONTENTS:
        #1. NO ENTRIES MESSAGE
        self.myNoEntriesLabel=QLabel()
        if fio.getNrOfEntries("TextFiles/Entries")==0:
            self.myNoEntriesLabel.setText("No entries")
        self.myNoEntriesLabel.setFont(QFont("Helvetica",dim.LARGE_FONT_SIZE))
        self.myNoEntriesLabel.setParent(self.myRightPanel)
        self.myNoEntriesLabel.move(90,50)

        #2. ENTRIES LIST: EACH ENTRY WILL BE A LABEL WITH THE TITLE OF THE ENTRY + BUTTON TO LOAD (max 5 entries)
        if not fio.getNrOfEntries("TextFiles/Entries")==0:
            myPackedResults=fn.initButtons(self.myRightPanel,fio.getNrOfEntries("TextFiles/Entries"))
            self.myRightPanel.setLayout(myPackedResults[0])
            self.rightPanelBtnList=myPackedResults[1]

        #RIGHT VBOX
        self.myRightVBoxLayout=QVBoxLayout()


        # BRIDGE HBOX
        self.myBridgeHBoxLayout = QHBoxLayout()
        self.myBridgeHBoxLayout.insertSpacing(0,dim.LARGE_SPACE)
        self.myBridgeHBoxLayout.insertLayout(2,self.myRightVBoxLayout)


        #LEFT VBOX LAYOUT -- MAIN LAYOUT
        self.myLeftVBoxLayout=QVBoxLayout()
        self.myLeftVBoxLayout.insertSpacing(0,dim.LARGE_UI_GAP)
        self.myLeftVBoxLayout.insertLayout(1,self.myLeftHBoxLayout1)
        self.myLeftVBoxLayout.insertSpacing(2,dim.LARGE_UI_GAP)
        self.myLeftVBoxLayout.insertLayout(3,self.myLeftHBoxLayout2)
        self.myLeftVBoxLayout.insertSpacing(4,dim.LARGE_UI_GAP)
        self.myLeftVBoxLayout.insertWidget(5,self.myTitleTextbox)
        self.myLeftVBoxLayout.insertWidget(6,self.myBodyTextbox)
        self.myLeftVBoxLayout.insertStretch(7)

        self.myLeftVBoxLayout.insertLayout(8,self.myBridgeHBoxLayout)
        self.myLeftVBoxLayout.setContentsMargins(dim.LARGE_UI_GAP,0,0,0)


        #UNITE ALL LAYOUTS
        self.myMainWidget.setLayout(self.myLeftVBoxLayout)

        #TIMER
        self.myTimer=QTimer()
        self.myTimer.timeout.connect(self.processQueue)
        self.myTimer.start(100)

        self.mySlowTimer=QTimer()
        self.mySlowTimer.timeout.connect(self.updateUI)
        self.mySlowTimer.start(300)

        self.setCentralWidget(self.myMainWidget)

    def processQueue(self):
        try:
            result=Dimensions.asyncQueue.get_nowait()
            if result == "summonRightPanel":
                self.myRightPanel.setFocus()
                if self.showFlag == False:
                    fn.moveRightPanel(self.myRightPanel, startPos=self.rightPanelDocked, endPos=self.rightPanelVisible,showFlag=True)
                    self.showFlag=True
            if result == "hideRightPanel":
                if self.showFlag == True:
                    fn.moveRightPanel(self.myRightPanel, startPos=self.rightPanelDocked, endPos=self.rightPanelVisible,showFlag=False)
                    self.showFlag=False
        except:
            pass

    def updateUI(self):
        fn.linkBtnConnectsToEntries(self.rightPanelBtnList,self.myBodyTextbox,self.myTitleTextbox,fio.getAllEntryNames("TextFiles/Entries"))

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress:
            if not self.myRightPanel.rect().contains(self.myRightPanel.mapFromGlobal(event.globalPos())) and not self.myLoadButton.rect().contains(self.myLoadButton.mapFromGlobal(event.globalPos())):
                Process(fn.pushMessageToAsyncQueue(dim.asyncQueue,"hideRightPanel")).start()
        return super().eventFilter(obj, event)



if __name__=="__main__":
    myApp=QApplication(sys.argv)
    myWindow=MainWindow()
    myWindow.show()
    myApp.exec()

