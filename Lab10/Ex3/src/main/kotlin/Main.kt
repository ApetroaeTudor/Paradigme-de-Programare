package lab.pp

import kotlinx.coroutines.*
import kotlinx.coroutines.Runnable
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import java.util.LinkedList
import java.util.Queue
import java.util.concurrent.locks.ReentrantLock

val myLock = ReentrantLock()


suspend fun sum(n:Int){
    var returnVal:Int=0
    for(i in 0..n){
        returnVal+=i
    }
    println("Sum = $returnVal")
}

val ctx1 = newSingleThreadContext("myCtx1")
val ctx2 = newSingleThreadContext("myCtx2")
val ctx3 = newSingleThreadContext("myCtx3")
val ctx4 = newSingleThreadContext("myCtx4")

val myMutex = Mutex()

fun main() = runBlocking {
    var myQueue = LinkedList<Int>(listOf(100,200,300,400))
    val sumVals = LinkedList<Deferred<Int>>()
    val contexts = LinkedList<ExecutorCoroutineDispatcher>(listOf(ctx1,ctx2,ctx3,ctx4))

    for(i in 0..<4){
        val job = async(contexts[i]) {
            delay(500)
            println("Currently extracting val from queue on thread ${Thread.currentThread().name}")
            myMutex.withLock {
                val ret = myQueue.get(0)
                myQueue.pop()
                ret
            }
        }
        sumVals.add(job)
    }

    for(i in 0..<4){
        launch(contexts[i]) {
            println("Currently doing sum on thread ${Thread.currentThread().name}")
            sum(sumVals[i].await())
        }
    }

    delay(5000)
    println("Java style threads:\n")
    myQueue = LinkedList<Int>(listOf(100,200,300,400))



    class Task(val targetQueue:LinkedList<Int>) : Runnable{
        override fun run() {
            var extractedValue = -1
            while(true){
                if(!myLock.isLocked()){
                    myLock.lock()
                    extractedValue = targetQueue.get(0)
                    targetQueue.pop()
                    myLock.unlock()
                    break;
                }
                else{
                    Thread.sleep(200)
                }
            }
            println("task done on thread ${Thread.currentThread().name}: ${(0..extractedValue).sum()}")
        }
    }

    val myThread1 = Thread(Task(myQueue)); myThread1.name = "Thr1"; myThread1.start()
    val myThread2 = Thread(Task(myQueue)); myThread2.name = "Thr2"; myThread2.start()
    val myThread3 = Thread(Task(myQueue)); myThread3.name = "Thr3"; myThread3.start()
    val myThread4 = Thread(Task(myQueue)); myThread4.name = "Thr4"; myThread4.start()

    myThread1.join(); myThread2.join(); myThread3.join(); myThread4.join()







}

