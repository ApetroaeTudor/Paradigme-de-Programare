from abc import ABC
from typing import Optional
import re

import execution as e

def checkPythonCode(code:Optional['str'])->bool:
    for line in code.split('\n'):
        if "def" in line or "__" in line:
            return True
    return False

def checkKotlinCode(code:Optional['str'])->bool:
    for line in code.split('\n'):
        if "fun" in line:
            return True
    return False

def checkBashCode(code:Optional['str'])->bool:
    if "#!/" in code:
        return True
    return False

def checkJavaCode(code:Optional['str'])->bool:
    for line in code.split('\n'):
        if "public static void" in line:
            return True
    return False






class AbstractHandler:
    def __init__(self,
                 executor: Optional['e.Executor'],
                 next1: Optional['AbstractHandler'] = None,):
        self.next1 = next1
        self.executor = executor

    def handleRequest(self,file_to_check):
        pass

class PythonHandler(AbstractHandler):
    def handleRequest(self,file_to_check):
        if file_to_check:
            with open(file_to_check,'r') as f:
                if checkPythonCode(f.read()):
                    self.executor.command=e.PythonCommand(file_to_check)
                    self.executor.execute()
                else:
                    self.next1.handleRequest(file_to_check)

class KotlinHandler(AbstractHandler):
    def handleRequest(self, file_to_check):
        if file_to_check:
            with open(file_to_check,'r') as f:
                if checkKotlinCode(f.read()):
                    self.executor.command=e.KotlinCommand(file_to_check)
                    self.executor.execute()
                else:
                    self.next1.handleRequest(file_to_check)

class BashHandler(AbstractHandler):
    def handleRequest(self, file_to_check):
        if file_to_check:
            with open(file_to_check,'r') as f:
                if checkBashCode(f.read()):
                    self.executor.command=e.BashCommand(file_to_check)
                    self.executor.execute()
                else:
                    self.next1.handleRequest(file_to_check)

class JavaHandler(AbstractHandler):
    def handleRequest(self, file_to_check):
        if file_to_check:
            with open(file_to_check,'r') as f:
                if checkJavaCode(f.read()):
                    self.executor.command=e.JavaCommand(file_to_check)
                    self.executor.execute()
                else:
                    print("Invalid file, can't execute")


        