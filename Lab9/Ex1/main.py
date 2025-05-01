import handlers as h
import execution as e

if __name__ == '__main__':
    file1 = "file1" #python
    file2 = "file2" #Kotlin
    file3 = "file3" #Bash
    file4 = "file4" #Java

    executor = e.Executor()

    python_handler = h.PythonHandler(executor)
    kotlin_handler = h.KotlinHandler(executor)
    bash_handler = h.BashHandler(executor)
    java_handler = h.JavaHandler(executor)

    python_handler.next1 = kotlin_handler
    kotlin_handler.next1 = bash_handler
    bash_handler.next1 = java_handler

    python_handler.handleRequest(file4)