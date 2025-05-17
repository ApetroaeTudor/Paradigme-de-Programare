package lab.pp

import java.awt.Point
import kotlin.math.atan2
import kotlin.math.sqrt

fun java.awt.Point.PRINT(){
    print("  (${this.x}:${this.y})  " )
}

fun java.awt.Point.DISTANCE(otherPct:Point):Double{
    return sqrt(((otherPct.x-this.x)*(otherPct.x-this.x) +(otherPct.y - this.y)*(otherPct.y-this.y)).toDouble() )
}

fun main(){
    val nrPct = 4
    val myList = mutableListOf<Point>(Point(0,2),  Point(1,2),  Point(2,-1),  Point(2,0),  Point(1,0))

    mutableListOf<Point>(Point(0,2),  Point(1,2),  Point(2,-1),  Point(2,0),  Point(1,0))
        .sortedBy { atan2( (it.y -myList.map { pct->pct.y }.average() ) ,(it.x - myList.map { pct->pct.x }.average())) }
        .zipWithNext()
        .also { it.forEach {elem-> elem.first.PRINT();  print("---"); elem.second.PRINT(); println(); } }
        .map{ pair -> pair.first.DISTANCE(pair.second)}
        .also { println("Distances: ${it}") }
        .fold(0.0){acc,it->acc+it}
        .also { println(it) }
        .also { println("Se adauga si ultima linie care a fost omisa de zipWithNext: ${it+myList
            .sortedBy {atan2( (it.y -myList.map { pct->pct.y }.average() ) ,(it.x - myList.map { pct->pct.x }.average()))  }
            .let{ list->
                val a = list.first()
                val b = list.last()
                    a.DISTANCE(b)}}")}
}