package lab.pp

import kotlinx.coroutines.*
import kotlinx.coroutines.Runnable
import java.util.LinkedList
import java.util.concurrent.locks.ReentrantLock
import kotlin.concurrent.withLock

suspend fun multiply(alpha:Int,myList: LinkedList<Int>){
    for(i in 0..<myList.size){
        myList.set(i,myList.get(i)*alpha)
    }
}

suspend fun order(myList: LinkedList<Int>){
    myList.sort()
}

val ctx1 = newSingleThreadContext("ctx1")
val ctx2 = newSingleThreadContext("ctx2")
val ctx3 = newSingleThreadContext("ctx3")

val lock = ReentrantLock()



fun main() = runBlocking {
    val myList = LinkedList<Int>(listOf(2,1,5,110,3))
    val alpha = 2;


    val job1 = launch(ctx1) {
        delay(500)
        multiply(alpha,myList)
        println("Job 1 -- multiplying done on thread ${Thread.currentThread().name}\n")
    }

    job1.join()

    val job2 = launch(ctx2) {
        delay(500)
        order(myList)
        println("Job 2 -- ordering done on thread ${Thread.currentThread().name}\n")
    }

    job2.join()

    val job3 = launch(ctx3) {
        delay(500)
        myList.forEach{
            print("$it ")
        }
        println("Job 3 -- printing done on thread ${Thread.currentThread().name}\n")
    }

    job3.join()



    println("Ex cu corutine e finalizat\n")
    delay(1000)

    class task1(val targetList:LinkedList<Int>,val alpha:Int) : Runnable{
        override fun run() {
            println("Job 1 -- multiplying done on thread ${Thread.currentThread().name}\n")
            lock.withLock {
                for(i in 0..<myList.size){
                    myList.set(i,myList.get(i)*alpha)
                }
            }
        }
    }

    class task2(val targetList:LinkedList<Int>) : Runnable{
        override fun run() {
            println("Job 2 -- ordering done on thread ${Thread.currentThread().name}\n")
            lock.withLock {
                myList.sort()
            }
        }
    }

    class task3(val targetList: LinkedList<Int>) : Runnable{
        override fun run() {
            println("Job 3 -- printing done on thread ${Thread.currentThread().name}\n")
            lock.withLock {
                myList.forEach{ print("$it ") }
            }
        }
    }

    val myThread1 = Thread(task1(myList,alpha))
    myThread1.name = "JavaStyleThread1"

    val myThread2 = Thread(task2(myList))
    myThread2.name = "JavaStyleThread2"

    val myThread3 = Thread(task3(myList))
    myThread3.name = "JavaStyleThread3"

    myThread1.start()
    myThread2.start()
    myThread3.start()

    ctx1.close()
    ctx2.close()
    ctx3.close()

}