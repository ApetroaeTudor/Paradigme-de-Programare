package lab.pp

import java.io.File
import kotlin.system.exitProcess

fun main(){
    val offset = 1
    val txtPath = "myTextFile.txt"
    val myFile = File(txtPath)
    if(!myFile.exists()){
        println("Error on opening file")
        exitProcess(-1)
    }
    val str = myFile.readText()
        .split("\n"," ")
        .forEach { word->
            if(word.length>=4 && word.length<=7 ){
                word.asSequence()
                    .map { ch->
                        when{
                            ch.isUpperCase()->{ ('A'.code + (ch.code-'A'.code + offset)%26 ).toChar()}
                            ch.isLowerCase()->{('a'.code + (ch.code-'a'.code + offset)%26 ).toChar()}
                            else -> {'x'}
                        }
                    }
                    .joinToString("")
                    .also { println(it) }
            }
            else{
                println(word)
            }

        }

}
