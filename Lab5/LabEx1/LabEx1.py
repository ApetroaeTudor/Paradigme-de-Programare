import tkinter
import tkinter as tk
import EventHandlers

import AsyncQueue

class baseFrame:

    def __init__(self,ROOT):

        self.root=ROOT
        self.root.geometry("1000x450")

        self.labelGuide=tkinter.Label(master=self.root,text="Input integer list: ")

        self.integerList=tkinter.Text(master=self.root,width=60,height=1)
        self.integerList.insert(tk.END,"Insert your list here..")
        self.integerList.bind("<FocusIn>", EventHandlers.FocusInRemoveText(self.integerList))
        self.integerList.bind("<FocusOut>", EventHandlers.FocusOutAddText(self.integerList))

        self.collectedLists=tkinter.Text(master=self.root,width=60,height=5)
        self.collectedLists.config(state="disabled")

        self.errorTag=tk.Label(master=self.root,text="")
        self.errorTag.config(text=f"Error: Non-Integer type characters found!")
        self.errorTag.config(bg="red")


        self.insertListButton=tkinter.Button(master=self.root,
                                            text="InsertList",
                                            command=lambda:EventHandlers.addTextToTextBox(
                                                                                    self.integerList,
                                            self.collectedLists,self.errorTag)
                                            )
        self.integerList.bind("<Return>",lambda event:EventHandlers.addTextToTextBox(
                                                                                    self.integerList,
                                            self.collectedLists,self.errorTag))
        self.updateGrid()

        self.root.after(200, self.updateUI)

    def updateGrid(self):
        self.labelGuide.grid(row=0, column=0, padx=10, pady=10)
        self.integerList.grid(row=0, column=1, padx=10, pady=10)
        self.collectedLists.grid(row=1, column=1, padx=10, pady=0)
        self.insertListButton.grid(row=0, column=2, padx=10, pady=10)

    def updateUI(self):
        try:
            result = AsyncQueue.asyncQueue.get_nowait()
            if result=="insertListError":
                self.errorTag.grid_forget()
        except:
            pass
        self.root.after(200, self.updateUI)



if __name__ == "__main__":
    ROOT=tk.Tk()
    base=baseFrame(ROOT)
    ROOT.mainloop()




