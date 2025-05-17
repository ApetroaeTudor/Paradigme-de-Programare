package lab.pp
import kotlin.text.chunked

fun main(){
    val myList = mutableListOf(1,21,75,39,7,2,35,3,31,7,8)
        .filter { it>5 }
        .also { println(it) }
        .chunked(2)
        .also { println(it) }
        .map{it[0]*it[1]}
        .also { println(it) }
        .fold(0){acc,i ->acc+i}
        .also { println(it) }

}