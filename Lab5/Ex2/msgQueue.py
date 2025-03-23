from multiprocessing import Queue, Process

def putMsgToQueue(msg:str,q:Queue):
    q.put(msg)

asyncQueue=Queue()
