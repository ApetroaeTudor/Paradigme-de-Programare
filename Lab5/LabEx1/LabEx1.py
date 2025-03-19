import tkinter as tk
import EventHandlers

import AsyncQueue

class baseFrame:

    def __init__(self,ROOT):

        #ROOT
        self.root=ROOT
        self.root.geometry("960x300")
        self.root.resizable(False,False)
        self.root.title("ListManager")


        #GUIDE LABEL
        self.labelGuide=tk.Label(master=self.root,text="Input integer list: ")


        #RESULT LABEL
        self.labelResult=tk.Label(master=self.root,text="Result:")

        #INTEGER LIST
        self.integerList=tk.Text(master=self.root,width=60,height=1)
        self.integerList.insert(tk.END,"Insert your list here..")
        self.integerList.bind("<FocusIn>", EventHandlers.FocusInRemoveText(self.integerList))
        self.integerList.bind("<FocusOut>", EventHandlers.FocusOutAddText(self.integerList))

        #VIEW NUMBERS TEXTBOX
        self.collectedLists=tk.Text(master=self.root,width=60,height=5)
        self.collectedLists.config(state="disabled")



        #ERROR TAG
        self.errorTag=tk.Label(master=self.root,text="")
        self.errorTag.config(text="")
        self.errorTag.config(bg="red")


        #RESULT TAB TEXTBOX
        self.resultTab=tk.Text(master=self.root,width=60,height=2)
        self.resultTab.config(state='disabled')
        #FILTERODD BUTTON
        self.filterOddButton=tk.Button(master=self.root,text="FilterOdd",command=lambda: EventHandlers.asyncProcessFunction(
                                                                                                                 self.collectedLists,
                                                                                                                 self.errorTag,
                                                                                                                 "No odd numbers found!",
                                                                                                                "odd"
        ))

        #FILTERPRIME BUTTON
        self.filterPrimeButton=tk.Button(master=self.root,text="FilterPrime",command=lambda: EventHandlers.asyncProcessFunction(
                                                                                                                        self.collectedLists,
                                                                                                                        self.errorTag,
                                                                                                                        "No prime numbers found!",
                                                                                                                        "prime"
        ))


        #SUM BUTTON
        self.sumButton=tk.Button(master=self.root,text="Sum",command=lambda: EventHandlers.asyncProcessFunction(
                                                                                                            self.collectedLists,
                                                                                                            self.errorTag,
                                                                                                            "No elements to sum",
                                                                                                            "sum"
        ))


        #INSERT LIST BUTTON
        self.insertListButton=tk.Button(master=self.root,
                                            text="InsertList",
                                            command=lambda:EventHandlers.addTextToTextBox(
                                                                                    self.integerList,
                                            self.collectedLists,self.errorTag,"Value is not of integer type"))

        #CLEAR EVERYTHING BUTTON
        self.clearListButton=tk.Button(master=self.root,text="CLEAR",command=lambda:EventHandlers.clearEverything(
                                                                                                                self.integerList,
                                                                                                                self.collectedLists,
                                                                                                                self.resultTab
        ))

        #ENTER KEY INSERTS NR
        self.integerList.bind("<Return>",lambda event:EventHandlers.addTextToTextBox(
                                                                                    self.integerList,
                                            self.collectedLists,self.errorTag,"Value is not of integer type"))


        self.updateGrid()
        self.root.after(200, self.checkQueue)

    def updateGrid(self):
        self.labelGuide.grid(row=0, column=0, padx=10, pady=10)
        self.integerList.grid(row=0, column=1, padx=10, pady=10)
        self.collectedLists.grid(row=1, column=1, padx=10, pady=0)
        self.insertListButton.grid(row=0, column=2, padx=10, pady=10)
        self.resultTab.grid(row=2,column=1,padx=10,pady=10)
        self.labelResult.grid(row=2,column=0,padx=10,pady=10)
        self.filterOddButton.grid(row=2,column=2,padx=10,pady=10)
        self.filterPrimeButton.grid(row=2,column=3,padx=10,pady=10)
        self.sumButton.grid(row=2,column=4,padx=10,pady=10)
        self.clearListButton.grid(row=3,column=0,padx=10,pady=10)

    def checkQueue(self):
        #EventHandlers.filterOdd(self.collectedLists,self.errorTag,"mda")
        try:
            result = AsyncQueue.asyncQueue.get_nowait()
            if "Error: " in result:
                self.errorTag.grid_forget()
            if "WidgetModification" in result:
                temp=result.split(".")
                if "showErrorTag" in result:
                    self.errorTag.config(text=temp[2])
                    self.errorTag.grid(row=3, column=1)
            if isinstance(result,list):
                temparr=''
                for elem in result:
                    temparr=str(elem)+' '+temparr
                self.resultTab.config(state='normal')
                self.resultTab.delete('1.0',tk.END)
                self.resultTab.insert(tk.END,temparr)
                self.resultTab.config(state='disabled')
        except:
            pass
        self.root.after(100, self.checkQueue)



if __name__ == "__main__":
    ROOT=tk.Tk()
    base=baseFrame(ROOT)
    ROOT.mainloop()




