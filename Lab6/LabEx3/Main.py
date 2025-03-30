from AudioFiles import *
from FileManipulator import getFileObject
if __name__=="__main__":

    filePaths=["AudioFiles/song1.flac","AudioFiles/song2.mp3","AudioFiles/song3.mp3","AudioFiles/song4.ogg","AudioFiles/song5.wav"]

    for file in filePaths:
        try:
            returnedObj=getFileObject(file)
            returnedObj.play()
        except Exception as e:
            print(f"Error: {e}")

