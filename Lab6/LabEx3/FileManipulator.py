import os
from AudioFiles import *

def getFileObject(filePath:str):
    if os.path.exists(filePath) and len(filePath.split("/")[len(filePath.split("/"))-1].split("."))>1:
        try:
            ext=filePath.split("/")[len(filePath.split("/"))-1].split(".")[1]
            FileName=filePath.split("/")[len(filePath.split("/"))-1]
            if(ext=="mp3"):
                return MP3File(FileName)
            elif(ext=="wav"):
                return WavFile(FileName)
            elif(ext=="ogg"):
                return OggFile(FileName)
            elif(ext=="flac"):
                return FlacFile(FileName)
        except Exception as e:
            print(f"Error: {e}")
    else:
        raise Exception("File doesn't exist or has no extension")