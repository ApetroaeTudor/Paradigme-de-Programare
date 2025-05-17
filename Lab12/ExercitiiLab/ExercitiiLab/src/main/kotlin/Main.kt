package lab.pp

import java.time.LocalDate
import java.time.format.DateTimeFormatter
import kotlin.math.sqrt
import kotlin.properties.Delegates

fun Int.checkIfPrime(): Boolean{ //ex1
    if(this<=1) {return false}
    if(this == 2) {return true}
    if(this%2 ==0){return false}
    val maxDiv = sqrt(this.toDouble()).toInt()
    for(div in 3..maxDiv){
        if(this%div == 0){
            return false
        }
    }
    return true
}

fun String.convertToDate(formatter:DateTimeFormatter):LocalDate{ //ex2
        return LocalDate.parse(this,formatter)
}

val myMap = mapOf( 1 to "abc", 2 to "def", 3 to "ghi"); //ex3
fun <A,B>Map<A,B>.reverseKeys() : Map<B,A>{
    val newMap:MutableMap<B,A> = mutableMapOf()
    this.map { entry -> newMap.put(entry.value,entry.key)   }
    return newMap
}

var myNr: Int by Delegates.vetoable(5){ //ex4
    property, oldValue, newValue ->
    newValue.checkIfPrime()
}


val myList = listOf(1,2,3)
fun <T> List<T>.duplicateBy(n:Int) : List<T>{ //ex5
    return this.flatMap { elem ->
        var intermediaryList = mutableListOf<T>()
        for(i in 0..<n){
            intermediaryList.add(elem)
        }
        intermediaryList
    }
}

val myString = "aaaabbbcc" //trb sa se elimine caracterele duplicate
fun String.removeDuplicateCharacters() : String{ //ex 6
    return this.asSequence().distinct().joinToString("")
}

val myString1 = "aaaabbbccdaaa"
fun String.shortenString() : String{ //ex7
    val returnVal:StringBuilder = StringBuilder()
    var lastChar = 'a'
    var count = 0

    this.asSequence().forEach {
        if(it!=lastChar){
            if(count>1){
                returnVal.append("${lastChar}${count}")
            }
            else{
                returnVal.append("${lastChar}")
            }
            count = 0
        }
        count++
        lastChar = it
    }

    if(count>1){
        returnVal.append("${lastChar}${count}")
    }
    else{
        returnVal.append("${lastChar}")
    }

    return returnVal.toString()
}

fun main(){
    val x = 5;
    val date = "2023-12-23"
    try {
        println(date.convertToDate(DateTimeFormatter.ISO_DATE))
    }
    catch (e:Exception){
        println("Please input a valid date")
    }

    myMap.reverseKeys().forEach{ println("${it.key}: ${it.value}") }

    myNr = 4
    println(myNr)
    myNr = 7
    println(myNr)

    println( myList.duplicateBy(5))
    println(myString.removeDuplicateCharacters())


    println(myString1.shortenString())
}