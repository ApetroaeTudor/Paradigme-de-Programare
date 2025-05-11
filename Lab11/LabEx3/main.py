from queue import Queue
import threading

queue_thr1_thr2 = Queue()
queue_thr2_thr3 = Queue()
ALPHA = 2



my_array = [2,1,4,5,2,0,12]

def multiplyWithAlpha(q_out):
    my_array_cpy = my_array.copy()
    for i in range(len(my_array_cpy)):
        my_array_cpy[i]*=ALPHA
    q_out.put(my_array_cpy)
    q_out.put(None)
        
def sorting(q_in,q_out):
    while True:
        item = q_in.get()
        if item is None:
            q_out.put(None)
            break
        item.sort()
        q_out.put(item)
        q_out.put(None)
    
def printing(q_in):
    while True:
        item = q_in.get()
        if item is None:
            break
        print(item)
    
if __name__ == "__main__":
    thread1 = threading.Thread(target=multiplyWithAlpha,args=(queue_thr1_thr2,))
    thread2 = threading.Thread(target=sorting,args=(queue_thr1_thr2,queue_thr2_thr3))
    thread3 = threading.Thread(target=printing,args=(queue_thr2_thr3,))
    
    thread1.start()
    thread2.start()
    thread3.start()
    
    thread1.join()
    thread2.join()
    thread3.join()