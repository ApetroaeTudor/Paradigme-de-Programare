package lab.pp

import kotlinx.coroutines.*
import java.util.*
import java.util.concurrent.atomic.AtomicInteger
import kotlin.system.*

import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import java.io.File
import java.io.FileWriter


val fileWriter = FileWriter("output.txt",true)

suspend fun writeToFile(chunk:List<Int>){
        //aici vine scrierea propriu-zisa
    fileWriter.write(chunk.joinToString("\n")+"\n")
}

suspend fun CoroutineScope.massiveRun(action: suspend() -> Unit){
    val n = 100
    val k = 1000

    val time = measureTimeMillis {
        val jobs = List(n){
            async {
                repeat(k){
                    action()
                }
            }
        }
        jobs.forEach{it.join()}
    }
    println("S-au efectuat ${n*k} operatii in $time ms")
}

val writerCount = 3

val mtContext = newFixedThreadPoolContext(5,"mtPool")
val writerContext = newFixedThreadPoolContext(writerCount,"file-writers")


//atomic integer garanteaza ca operatiile de scriere sunt indivizibile
//nu au loc intreruperi, e non blocking
//sunt folosite bariere de memorie - un store barrier obliga scrierile sa fie scrise direct in ram
var counter = AtomicInteger(0)

val myList = LinkedList<Int>()
val myMutex = Mutex()
val writeRatio =10000/ writerCount

fun main() = runBlocking<Unit> {

    withContext(Dispatchers.Default){
        massiveRun {
            val newValue = counter.incrementAndGet()
            myMutex.withLock { myList.add(newValue) }
        }
    }

    val chunks = myList.chunked(writeRatio)

    val writeTime = measureTimeMillis {
        val writeJobs = chunks.map{
            chunk->launch(writerContext){
                writeToFile(chunk)
                println("Threadul ${Thread.currentThread().name} a scris ${writeRatio} numere")
            }
        }

        writeJobs.forEach {
            it.join()
        }

    }



    println("Scrierea se realizeaza in $writeTime ms")
    fileWriter.close()

}