import random
from pathlib import Path
import os

def getRandomLineFromFile(filePath:str)->str:
    with open(filePath,"r") as myFile:
        myContent=myFile.readlines()
        return myContent.pop(random.randrange(0, len(myContent)))

def getNrOfEntries(dirPath:str)->int:
    return sum(1 for file in Path(dirPath).iterdir() if file.is_file())

def getAllEntryNames(dirPath:str)->list:
    myList=[]
    for file in Path(dirPath).iterdir():
        if file.is_file():
            myList.append(os.path.basename(file))
    return myList

def readContentFromFile(fileTitle:str)->str:
    filePath="TextFiles/Entries/" + fileTitle
    myContent=""
    with open(filePath,"r") as myFile:
        myContent=myContent+myFile.read()
    return myContent

def writeContentToCitate(Content:str):
    with open("TextFiles/Citate.txt","a") as file:
        file.write("\n"+Content)