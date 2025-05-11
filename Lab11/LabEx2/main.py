from threading import Thread, Condition
import time
from queue import Queue


class Consumator(Thread):
    def __init__(self,condition,interProcessQueue,maxBufferSize,maxNrOfConsumes):
        Thread.__init__(self)
        self.condition = condition
        self.interProcessQueue = interProcessQueue
        self.maxBufferSize = maxBufferSize
        self.maxNrOfConsumes = maxNrOfConsumes

    def consumator(self):
        self.condition.acquire()
        if self.interProcessQueue.qsize() == 0:
            self.condition.wait()
            print('mesaj de la consumator: nu am nimic disponibil')
        self.interProcessQueue.get()
        print('mesaj de la consumator : am utilizat un element')
        print('mesaj de la consumator : mai am disponibil', self.interProcessQueue.qsize(),
              'elemente')
        self.condition.notify()
        self.condition.release()

    def run(self):
        for i in range(self.maxNrOfConsumes):
            self.consumator()


class Producator(Thread):
    def __init__(self,condition,interProcessQueue,maxBufferSize,maxNrOfProduces):
        Thread.__init__(self)
        self.condition = condition
        self.interProcessQueue = interProcessQueue
        self.maxBufferSize = maxBufferSize
        self.maxNrOfProduces = maxNrOfProduces

    def producator(self):
        self.condition.acquire()
        if self.interProcessQueue.qsize() == maxBufferSize:
            self.condition.wait()
            print('mesaj de la producator : am disponibile', self.interProcessQueue.qsize(),
                  'elemente')
            print('mesaj de la producator : am oprit productia')
        self.interProcessQueue.put(1)
        print('mesaj de la producator : am produs', self.interProcessQueue.qsize(), 'elemente')
        self.condition.notify()
        self.condition.release()

    def run(self):
        for i in range(self.maxNrOfProduces):
            self.producator()


if __name__ == '__main__':
    maxBufferSize = 7
    interProcessQueue = Queue(maxsize=maxBufferSize)
    myCondition = Condition()
    maxNumberOfConsumes = 10
    maxNumberOfProduces = 10 
    
    
    producator = Producator(myCondition,interProcessQueue,maxBufferSize,maxNumberOfProduces)
    consumator = Consumator(myCondition,interProcessQueue,maxBufferSize,maxNumberOfConsumes)
    producator.start()
    consumator.start()
    producator.join()
    consumator.join()