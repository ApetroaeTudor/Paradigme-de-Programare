import time
import tkinter as tk
import multiprocessing as mp

import AsyncQueue

def sleepThread(q):
    time.sleep(0.5)
    q.put("insertListError")

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

def addTextToTextBox(myIntegerList:tk.Text, myTextBox:tk.Text,errorTag:tk.Label):
    nrOfLines= int(myTextBox.index("end").split(".")[0]) - 1
    textToInsert=myIntegerList.get("1.0",tk.END).strip().replace(',',' ')

    for myChar in textToInsert.strip().replace(' ',''):
        if not myChar.isdigit():
            myIntegerList.delete("1.0",tk.END)
            errorTag.grid(row=2, column=1, padx=10, pady=10)
            myProcess=mp.Process(target=sleepThread,args=(AsyncQueue.asyncQueue,))
            myProcess.start()
            return


    if nrOfLines<6 and textToInsert:
        if not textToInsert == "Insertyourlisthere..":
            myTextBox.config(state="normal")
            myTextBox.insert(tk.END,textToInsert+"\n")
            myTextBox.config(state="disabled")
            myIntegerList.delete("1.0",tk.END)

