import math
import multiprocessing
import time
import tkinter as tk
import multiprocessing as mp

import AsyncQueue

def errorThread(q:multiprocessing.Queue,errorMessage):
    time.sleep(1)
    q.put("Error: "+ errorMessage)

def processListsThread(q:multiprocessing.Queue,myList:list):
    q.put(myList)

def FocusInRemoveText(myTextBox: tk.Text):
    def handler(event):
        if myTextBox.get("1.0",tk.END).strip()=="Insert your list here..":
            myTextBox.delete("1.0",tk.END)
    return handler

def FocusOutAddText(myTextBox: tk.Text):
    def handler(event):
        if not myTextBox.get("1.0",tk.END).strip():
            myTextBox.insert(tk.END,"Insert your list here..")
    return handler

def addTextToTextBox(myIntegerList:tk.Text, myTextBox:tk.Text,errorTag:tk.Label,errorText:str):
    nrOfLines= int(myTextBox.index("end").split(".")[0]) - 1
    textToInsert=myIntegerList.get("1.0",tk.END).strip().replace(',',' ')

    for myChar in textToInsert.strip().replace(' ',''):
        if not myChar.isdigit():
            myIntegerList.delete("1.0",tk.END)
            errorTag.config(text=errorText)
            errorTag.grid(row=3, column=1)
            myProcess=mp.Process(target=errorThread,args=(AsyncQueue.asyncQueue,errorText))
            myProcess.start()
            return


    if nrOfLines<6 and textToInsert:
        if not textToInsert == "Insertyourlisthere..":
            myTextBox.config(state="normal")
            myTextBox.insert(tk.END,textToInsert+"\n")
            myTextBox.config(state="disabled")
            myIntegerList.delete("1.0",tk.END)

def asyncProcessFunction(myIntegerList: tk.Text, errorTag: tk.Label, errorText: str,filterType):
    if filterType == "odd":
        myAsyncProcess = mp.Process(target=filterOdd, args=(myIntegerList, errorTag, errorText,AsyncQueue.asyncQueue))
        myAsyncProcess.start()
    else:
        if filterType=="prime":
            myAsyncProcess=mp.Process(target=filterPrime(myIntegerList,errorTag,errorText,AsyncQueue.asyncQueue))
            myAsyncProcess.start()
        else:
            if filterType=="sum":
                myAsyncProcess = mp.Process(target=sum(myIntegerList, errorTag, errorText, AsyncQueue.asyncQueue))
                myAsyncProcess.start()



def filterOdd(myIntegerList:tk.Text,errorTag:tk.Label,errorText:str,q:mp.Queue):
    myText=myIntegerList.get("1.0",tk.END).strip().replace('\n', ' ')
    myText=myText.replace(',',' ')
    myText=myText.split(" ")
    myOddList=[]
    for stri in myText:
        if stri:
            if not int(stri) %2 ==0:
                myOddList.insert(0,int(stri))
    if myOddList:
        q.put(myOddList)
    else:
        q.put("WidgetModification.showErrorTag."+errorText)

        myProcess=mp.Process(target=errorThread,args=(q,errorText))
        myProcess.start()
        return

def filterPrime(myIntegerList:tk.Text,errorTag:tk.Label,errorText:str,q:mp.Queue):
    myText = myIntegerList.get("1.0", tk.END).strip().replace('\n', ' ')
    myText = myText.replace(',', ' ')
    myText = myText.split(" ")
    myPrimeList = []
    for stri in myText:
        if stri:
            isPrime=True
            for i in range (2,int(math.sqrt(int(stri))+1)):
                if int(stri) % i ==0:
                    isPrime=False
                    break

            if int(stri)==2:
                isPrime=True
            if int(stri)<2:
                isPrime=False
            if(isPrime==True):
                myPrimeList.append(int(stri))
    if myPrimeList:
        q.put(myPrimeList)
    else:
        q.put("WidgetModification.showErrorTag."+errorText)

        myProcess=mp.Process(target=errorThread,args=(q,errorText))
        myProcess.start()
        return

def sum(myIntegerList:tk.Text,errorTag:tk.Label,errorText:str,q:mp.Queue):
    myText = myIntegerList.get("1.0", tk.END).strip().replace('\n', ' ')
    myText = myText.replace(',', ' ')
    myText = myText.split(" ")
    if len(myText) == 0:
        q.put("WidgetModification.showErrorTag." + errorText)
        myProcess = mp.Process(target=errorThread, args=(q, errorText))
        myProcess.start()
        return

    mySum = []
    sum=int(0)
    for stri in myText:
        if stri:
            sum=sum+int(stri)
    mySum.append(sum)
    q.put(mySum)

def clearEverything(myIntegerList:tk.Text,myCollectedText:tk.Text,myResultText:tk.Text):
    if not 'Insert your list here..' in myIntegerList.get('1.0','2.0'):
        myIntegerList.delete('1.0',tk.END)
    myCollectedText.config(state='normal')
    myCollectedText.delete('1.0',tk.END)
    myCollectedText.config(state='disabled')

    myResultText.config(state='normal')
    myResultText.delete('1.0',tk.END)
    myResultText.config(state='disabled')