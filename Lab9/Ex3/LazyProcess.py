from multiprocessing import Process

class LazyProcess:
    def __init__(self):
        self.process = None
        self.task = None
        self.args = ()

    def set_behavior(self,task,args):
        self.task = task
        self.args = args
        self.process = Process(target=self.task,args=(self.args,))
    
    def start(self):
        if self.process is None:
            raise Exception("Task not defined")
        self.process.run()

    def join(self):
        if self.process is not None:
            self.process.join()