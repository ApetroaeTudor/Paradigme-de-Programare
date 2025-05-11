import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import time
import random


threadingLock = threading.Lock()
multiprocessingLock = multiprocessing.Lock()

myArray = []
for i in range(1,100000):
    myArray.append(random.uniform(0,1000))


myListSize = 10000000
myEmptyArray = []
for i in range(1,myListSize):
    myEmptyArray.append(0)


def incByOne(collection,lock):
    with lock:
        for i in range(0,len(myEmptyArray)):
            collection[i]= collection[i]+1




def squared(collection):
    return [x**2 for x in collection]

def sort(collection):
    collection.sort()

def ver_1():
    # thread_1 = threading.Thread(target=sort,args=(squared(myArray.copy()),))
    # thread_2 = threading.Thread(target=sort,args=(squared(myArray.copy()),))
    global myEmptyArray
    thread_1 = threading.Thread(target=incByOne,args=(myEmptyArray,threadingLock))
    thread_2 = threading.Thread(target=incByOne,args=(myEmptyArray,threadingLock))
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()


def ver_2():
    global myEmptyArray
    # sort(squared(myArray.copy()))
    # sort(squared(myArray.copy()))
    incByOne(myEmptyArray,threadingLock)
    incByOne(myEmptyArray,threadingLock)


def ver_3():
    global myEmptyArray
    # process_1 = multiprocessing.Process(target=sort,args=(squared(myArray.copy()),))
    # process_2 = multiprocessing.Process(target=sort,args=(squared(myArray.copy()),))
    process_1 = multiprocessing.Process(target=incByOne,args=(myEmptyArray,multiprocessingLock))
    process_2 = multiprocessing.Process(target=incByOne,args=(myEmptyArray,multiprocessingLock))
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()


def ver_4():
    global myEmptyArray
    with ThreadPoolExecutor(max_workers=2) as executor:
        future = executor.submit(incByOne(myEmptyArray,threadingLock))
        future = executor.submit(incByOne(myEmptyArray,threadingLock))


if __name__ == '__main__':
    start = time.time()
    ver_1()
    end = time.time()
    print("\n Timp executie pseudoparalelism cu GIL")
    print(end - start)
    start = time.time()
    ver_2()
    end = time.time()
    print("\n Timp executie secvential")
    print(end - start)
    start = time.time()
    ver_3()
    end = time.time()
    print("\n Timp executie paralela cu multiprocessing")
    print(end - start)
    start = time.time()
    ver_4()
    end = time.time()
    print("\n Timp executie paralela cu concurrent.futures")
    print(end - start)