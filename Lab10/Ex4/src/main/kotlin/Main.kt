package lab.pp
import java.io.File
import java.util.LinkedList
import kotlinx.coroutines.*
import kotlinx.coroutines.Runnable
import java.util.concurrent.*

val files = LinkedList<File>(listOf(File("file1.txt"),File("file2.txt"),File("file3.txt")))

suspend fun readFromFiles(idx:Int){
        println("Read from file nr ${idx+1} on thread ${Thread.currentThread().name}: ${files[idx].readText()}")
}


fun main() = runBlocking {
    val myContext = Executors.newFixedThreadPool(4).asCoroutineDispatcher()
    for(i in 0..<3){
        launch(myContext) {
            readFromFiles(i)
        }
    }
    myContext.close()

    delay(400)
    println("Java style threads: ")

    class Task(val idx:Int):Runnable{
        override fun run() {
            println("Read from file nr ${idx+1} on thread ${Thread.currentThread().name}: ${files[idx].readText()}")
        }
    }

    val myExecutor = Executors.newFixedThreadPool(4)
    for(i in 0..<3){
        myExecutor.submit(Task(i))
    }

    //nu mai primeste noi taskuri, taskurile incepute deja continua sa ruleze
    myExecutor.shutdown()
    myExecutor.awaitTermination(5,TimeUnit.SECONDS)

    println("Task done")

}
