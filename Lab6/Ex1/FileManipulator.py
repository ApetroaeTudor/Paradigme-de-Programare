import os
from pathlib import Path
from unittest import expectedFailure
import struct

class FileManipulator:
    dirPath:str

    def __init__(self,dirPath):
        myPath=Path(dirPath)
        if myPath.is_dir():
            self.dirPath=dirPath
        else:
            raise Exception("Given path isn't a valid dir path")

    def findFileType(self,fileName:str):
        item=Path(fileName)
        if item.is_file():
            freqArr = [0.0] * 256

            # print(f"File title: {item}")

            with item.open('rb') as f:
                byte=f.read(1)
                while byte:
                    freqArr[byte[0]]+=1
                    byte=f.read(1)
            isASCII=self.checkASCII(freqArr)
            isUNICODE_UTF16=self.checkUNICODE_UTF16(freqArr)
            isBinary=self.checkBinary(freqArr)

            if isUNICODE_UTF16:
                return ("UNICODE",str(fileName),freqArr)
            elif isASCII:
                isXML=self.checkXML(freqArr)
                if isXML:
                    textcontent=item.read_text()
                    mainTag=textcontent.split("<")[1]
                    mainTag=textcontent.split(">")[0]
                    mainTag=mainTag.replace("<",'')
                    return ("XML",str(fileName),freqArr,mainTag)
                else:
                    return ("ASCII",str(fileName),freqArr)
            elif isBinary:
                with item.open('rb') as f:
                    isBMP= (f.read(2) == b'BM')
                    if(isBMP):
                        BMPData=self.getBMPData(item)
                        return ("BMP",str(fileName),freqArr,BMPData[0],BMPData[1],BMPData[2])
                    else:
                        return ("Binary",str(fileName),freqArr)
        else:
            raise Exception("invalid file")


    def processDir(self):
        myPath = Path(self.dirPath)
        resultList=[]
        for item in myPath.iterdir():
            currentItemResultTuple=self.findFileType(str(item))
            resultList.append(currentItemResultTuple)

        return resultList

    def checkASCII(self,freqArr:list[float]):
        sumOfAllFrequencies=sum(freqArr)
        sumOfRegularCharacterFrequencies=0
        sumOfRareCharacterFrequencies=0
        index=0
        while index < 256:
            if index==9 or index==10 or index==13 or (index >=32 and index<=127):
                sumOfRegularCharacterFrequencies+=freqArr[index]
            else:
                sumOfRareCharacterFrequencies+=freqArr[index]
            index+=1

        try:
            regularCharacterFrequency=((sumOfRegularCharacterFrequencies)/sumOfAllFrequencies)*100
            rareCharacterFrequency=((sumOfRareCharacterFrequencies/sumOfAllFrequencies))*100
            if regularCharacterFrequency >= 85 and rareCharacterFrequency <= 15:
                return True
        except ZeroDivisionError as e:
            print("Can't evaluate Empty file")
            return False

        return False

    def checkUNICODE_UTF16(self,freqArr:list[float]):
        sumOfAllFrequencies = sum(freqArr)
        sumOfZerosFrequencies = freqArr[0]
        try:
            zeroCharacterFrequency=(sumOfZerosFrequencies/sumOfAllFrequencies)*100
            if zeroCharacterFrequency >=30:
                return True
        except ZeroDivisionError as e:
            print("Can't evaluate Empty file")
            return False

        return False

    def checkBinary(self,freqArr:list[float]):
        expectedFrequency=sum(freqArr)/256
        acceptedDeviation=20
        index=1

        while index<256:
            if freqArr[index] < expectedFrequency-acceptedDeviation or freqArr[index] > expectedFrequency + acceptedDeviation:
                return False
            index+=1
        return True

    def checkXML(self,freqArr:list[float]):
        freqOfRightArrow=freqArr[ord('<')]
        freqOfLeftArrow=freqArr[ord('>')]
        expectedFrequency=sum(freqArr)/256


        if freqOfLeftArrow==freqOfRightArrow and freqOfRightArrow> expectedFrequency*5:
            return True
        return False

    def getBMPData(self,fileItem):
        with open(fileItem,"rb") as f:
            f.seek(18) #offset 18
            width=struct.unpack("<I", f.read(4))[0] #<I inseamna little endian < si interpretare ca Integer(4 bytes)
            height=struct.unpack("<I", f.read(4))[0]

            f.seek(28) # la offset 28 e data despre bits per pixel
            bpp=struct.unpack("<H",f.read(2))[0] # short Int (2 bytes) --> H

            return width,height,bpp


