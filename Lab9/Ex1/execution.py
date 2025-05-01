import subprocess

class AbstractCommand:
    def __init__(self,file_to_execute):
        self.file_to_execute = file_to_execute
    def execute(self):
        pass

class PythonCommand(AbstractCommand):
    def execute(self):
        subprocess.run(["python3",self.file_to_execute])

class KotlinCommand(AbstractCommand):
    def execute(self):
        subprocess.run(["mv", "{}".format(self.file_to_execute), "{}.kt".format(self.file_to_execute)])
        subprocess.run(["kotlinc","{}.kt".format(self.file_to_execute),"-include-runtime","-d","file.jar"])
        subprocess.run(["java","-jar","file.jar"])
        subprocess.run(["rm","file.jar"])
        subprocess.run(["mv", "{}.kt".format(self.file_to_execute), "{}".format(self.file_to_execute)])

class BashCommand(AbstractCommand):
    def execute(self):
        subprocess.run(["chmod","u+x",self.file_to_execute])
        subprocess.run(["./{}".format(self.file_to_execute)])

class JavaCommand(AbstractCommand):
    def execute(self):
        subprocess.run(["mv", "{}".format(self.file_to_execute), "{}.java".format(self.file_to_execute)])
        subprocess.run(["javac", "{}.java".format(self.file_to_execute)])
        subprocess.run(["java", "{}".format(self.file_to_execute)])
        subprocess.run(["rm", "{}.class".format(self.file_to_execute)])
        subprocess.run(["mv", "{}.java".format(self.file_to_execute), "{}".format(self.file_to_execute)])


class Executor:
    def __init__(self,command=None):
        self.command = command
    def execute(self):
        self.command.execute()