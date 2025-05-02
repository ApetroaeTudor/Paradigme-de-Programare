from abc import ABC,abstractmethod
import time 
import threading
import subprocess
import numpy
import Strategy as s

import LazyProcess as lp

time_quantum = int(2)
my_lock = threading.Lock()

requests_in_current_time_quantum = int(1)
requests_in_previous_time_quantum = int(1)
requests_queue = []

processes= []


def task(args:list):
    task = ["python3","main.py"]
    for arg in args:
        task.append(str(arg))
    subprocess.run(task)






def timer():
    global requests_in_current_time_quantum
    global requests_in_previous_time_quantum
    global requests_queue
    while True:
        time.sleep(time_quantum)
        with my_lock:
            print("\033[1m Time quantum elapsed -- \033[0m\nNr of requests: {}\n\n".format(requests_in_current_time_quantum-1))
            proxy.dispatcher_concrete.execute_requests()

            requests_in_previous_time_quantum = requests_in_current_time_quantum
            requests_in_current_time_quantum = 1
            requests_queue = []
            
        



class DispatcherAbstract(ABC):
    pass

class DispatcherConcrete(DispatcherAbstract):
    def __init__(self):
        self.strategy = s.NumpySplitStrategy()
        
    def execute_requests(self):
            global processes
            if requests_in_current_time_quantum > 2*requests_in_previous_time_quantum:
                print("\n\nCREATING NEW PROCESS\n\n")
                processes.append(lp.LazyProcess()) #doar ii dau append, folosesc un LazyProcess caruia ii voi da task mai tarziu si il voi porni mai tarziu
            if requests_in_current_time_quantum <= requests_in_previous_time_quantum/2:
                print("\n\nREMOVING A PROCESS\n\n")
                if len(processes) > 0:
                    processes.pop()
            if requests_in_current_time_quantum == 0:
                processes = []
            
            num_chunks = len(processes)

            fragmented_tasks_list = self.strategy.split_queue(requests_queue,num_chunks)
            
            for i in range(0,len(processes)):
                if i < len(fragmented_tasks_list):
                    processes[i].set_behavior(task,tuple(fragmented_tasks_list[i]))
                    processes[i].start()
                    print("\nStarted process nr {}\n\n".format(i+1))
                    

class Verifier(DispatcherAbstract):
    def __init__(self):
        self.dispatcher_concrete = DispatcherConcrete()
    
    def take_request(self,url):
        global requests_in_current_time_quantum
        global requests_queue
        with my_lock:
            requests_in_current_time_quantum+=1
            requests_queue.append(url)
            
            

proxy = Verifier()

if __name__ == '__main__':
    timer_thread = threading.Thread(target=timer)
    timer_thread.start()

    proxy.take_request("https://httpbin.org/get")
    proxy.take_request("https://catfact.ninja/fact")
    
    time.sleep(3)
    urls = ["https://api.github.com/zen","https://icanhazip.com/","https://checkip.amazonaws.com/","https://httpbin.org/uuid","https://official-joke-api.appspot.com/random_joke","https://dog.ceo/api/breeds/list/all"]
    for url in urls:
        proxy.take_request(url)



