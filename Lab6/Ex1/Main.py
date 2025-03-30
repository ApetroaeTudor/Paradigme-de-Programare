from FileManipulator import *
from FileClasses import *

if __name__=="__main__":

    try:
        myManipulator=FileManipulator("/home/tudor/AN2/PP/pp-1211b-homeworks-ApetroaeTudor/Lab6/Ex1/Files")
        packedData=myManipulator.processDir()
        myFiles=[]
        for data in packedData:
            
            temp="undefined"
            if data[0]=="UNICODE":
                temp=TextUNICODE(data[1],data[2])
            elif data[0]=="XML":
                temp=XMLFile(data[1],data[2],data[3])
            elif data[0]=="ASCII":
                temp=TextASCII(data[1],data[2])
            elif data[0]=="BMP":
                temp=BMP(data[1],data[2],data[3],data[4],data[5])
            elif data[0]=="Binary":
                temp=Binary(data[1],data[2])
            myFiles.append(temp)

        for file in myFiles:
            print()
            print(file)


    except:
        print("Error with file manipulation")

