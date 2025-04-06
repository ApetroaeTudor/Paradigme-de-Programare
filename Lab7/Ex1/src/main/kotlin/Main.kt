import kotlin.math.log

fun main() {
    val rawText = readFile("/var/log/apt/history.log")
    val entries = tokenizeEntries(rawText)
    val logRecords= mutableListOf<HistoryLogRecord>()
    entries.forEach(){
        val temp=HistoryLogRecord(it)
        logRecords.add(temp)
    }
    logRecords.forEach(){
        println(it)
    }
    println("\nMAP:\n")

    val myMap=makeHashMap(logRecords)
    myMap.forEach(){ (key,value)->
        print(key)
        println(" <---> $value")
        println()
    }

    println("\nCOMPAR LOG-URI DUPA TIMESTAMP: \n")
    val logs=myMap.values.sorted()
    logs.forEach(){
        println(it)
    }

    println("\nREPLACEMENT\n")


    replaceInMap(myMap.values.elementAt(0),myMap.values.elementAt(1),myMap)
}