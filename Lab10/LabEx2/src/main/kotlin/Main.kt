package lab.pp

import kotlinx.coroutines.*
import kotlin.system.*
import java.io.File

class Semafor private constructor(){
    companion object{
        val instance = Semafor()
        val fname = "Semafor.txt"
    }
    fun isLocked():Boolean{
        return !(File(fname).length() == 0L)
        //daca NU e gol atunci inseamna ca e locked
    }

    fun Lock():Boolean{
        if(!isLocked()){
            File(fname).writeText("lock")
            return true
        }
        return false
    }

    fun Unlock():Boolean{
        if(isLocked()){
            File(fname).writeText("")
            return true
        }
        return false
    }
}

val myContext = newFixedThreadPoolContext(5,"fileWriters")
val targetFileName = "TargetFile.txt"

suspend fun writeToFile(){
    withContext(myContext){
        while(true){
            if(Semafor.instance.Lock()){
                File(targetFileName).appendText("Acces in fisier de la threadul: ${Thread.currentThread().name}\n")
                Semafor.instance.Unlock()
                break;
            }
            else{
                delay(100)
            }
        }
    }
}

fun main(): Unit = runBlocking{
    val Jobs = List(10)
    {
        launch {
            writeToFile()
        }
    }

    Jobs.forEach {
        it.join()
    }

}

