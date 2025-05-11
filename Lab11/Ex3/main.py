import threading
import math
import time

def approximate_number(nr:float):
    if nr % 1 >= 0.5:
        return int(nr) + 1  
    else:
        return int(nr)  
    
# thread pool
# trb sa implementeze blocul with: cu __enter()__ si __exit()__ dar si terminate
# mecanism de load balancing cu map()
# join si terminate

class SignalingThread(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
        
        self.personalTaskList = []

        
    def run(self):
        for elem in self.personalTaskList:
            elem[0](*(elem[1:]))
            print("\nTask done on thread " + threading.current_thread().name + "\n")
        

    def add_task(self,task,args):
        self.personalTaskList.insert(0,(task,*args))



class MyThreadPool:
    def __init__(self, nr_of_threads:int):
        self.taskDictLock = threading.Lock()
        self.is_active = True
        self.threads = []
        for i in range(nr_of_threads):
            self.threads.append(SignalingThread( "Thread_"+str((i+1))))
    
        self.nr_of_threads = nr_of_threads
        
        
    def map(self,tasks:list,args:list[list]):
        if self.is_active:
            nr_of_passed_tasks = len(tasks)
            nr_of_tasks_per_thread = approximate_number(float(nr_of_passed_tasks)/float(self.nr_of_threads))
            print(nr_of_tasks_per_thread*self.nr_of_threads)
            print(nr_of_passed_tasks)
            if nr_of_tasks_per_thread < 1:
                for i in range(self.nr_of_threads):
                    if(i< len(tasks) and i<len(args)):
                        self.threads[i].add_task(tasks[i],args[i])
                # 1 task/thread, pt cate task-uri am
            elif int(nr_of_tasks_per_thread)*int(self.nr_of_threads) >= nr_of_passed_tasks:
                nr_of_distributed_tasks = int(0)
                for i in range(len(self.threads)):
                    if i == len(self.threads) - 1: #ult thread
                        for _ in range(nr_of_tasks_per_thread):
                            if nr_of_distributed_tasks <= nr_of_passed_tasks:
                                if(i<len(self.threads) and nr_of_distributed_tasks < len(tasks) and nr_of_distributed_tasks< len(args)):
                                    self.threads[i].add_task(tasks[nr_of_distributed_tasks],args[nr_of_distributed_tasks])
                                    nr_of_distributed_tasks+=1
                    else:
                        for _ in range(nr_of_tasks_per_thread):
                            if nr_of_distributed_tasks <= nr_of_passed_tasks:
                                if(i<len(self.threads) and nr_of_distributed_tasks<len(tasks) and nr_of_distributed_tasks<len(args)):
                                    self.threads[i].add_task(tasks[nr_of_distributed_tasks],args[nr_of_distributed_tasks])
                                    nr_of_distributed_tasks+=1
                        
                # ult thread primeste cu un task mai putin
            elif int(nr_of_tasks_per_thread)*int(self.nr_of_threads) < nr_of_passed_tasks:
                nr_of_distributed_tasks = int(0)
                for i in range(len(self.threads)):
                    if i == len(self.threads) - 1: #ult thread
                        for _ in range(nr_of_tasks_per_thread+1):
                            if nr_of_distributed_tasks <= nr_of_passed_tasks:
                                self.threads[i].add_task(tasks[nr_of_distributed_tasks],args[nr_of_distributed_tasks])
                                nr_of_distributed_tasks+=1
                    else:
                        for _ in range(nr_of_tasks_per_thread):
                            if nr_of_distributed_tasks <= nr_of_passed_tasks:
                                self.threads[i].add_task(tasks[nr_of_distributed_tasks],args[nr_of_distributed_tasks])
                                nr_of_distributed_tasks+=1
            
            for thread in self.threads:
                thread.start()
                #ult thread primeste cu un task mai mult
        
        # de ex pot sa am 5 taskuri pe 3 threaduri, vreau pe thread 1 sa am thread1: 2 task-uri, thread2: 2 task-uri, thread3: 1 task
        
    
    def join(self):
        if self.is_active:
            print("Pool is active: waiting for threads to complete..\n")
        else:
            print("Pool is terminated, waiting for threads to finish jobs..\n")
        
        for thread in self.threads:
            if thread.is_alive():
                thread.join()
            
            
    def terminate(self):
        self.is_active = False
        # for process in self.threads:
        #     process.join()
        
    def activate(self):
        self.is_active = True
    
    def __enter__(self):
        self.activate()
        return self
        
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.terminate()
        self.join()
        if exc_type:
            return False
        
        
def task1(arg1:str = None ,arg2:str = None):
    print("HelloFromTask1, with args: ")
    print(arg1 if arg1 else "not_defined" + " " + arg2 if arg2 else "not_defined")
    time.sleep(0.5)
def task2(arg1:str = None):
    print("HelloFromTask2, with args: ")
    print(arg1 if arg1 else "not_defined")
    time.sleep(0.5)
def task3():
    print("HelloFromTask3")
    time.sleep(0.5)
def task4(arg1:str = None,arg2:str = None):
    print("HelloFromTask4, with args: ")
    print(arg1 if arg1 else "not_defined"+ " " +arg2 if arg2 else "not_defined")
    time.sleep(0.5)
    

if __name__ == "__main__":
    
    
    with MyThreadPool(15) as pool:
        pool.map([task1,task2,task3,task4,task1,task3],[["hey","hello"],["salut"],[],["HELLOWORLD","hello_world"],[],[]])
        
    print("\n\nThis prints after the pool is terminated and all threads are joined")
        
    