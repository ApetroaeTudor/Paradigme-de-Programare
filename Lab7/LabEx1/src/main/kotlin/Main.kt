
fun main() {
    val entriesAsPlainString=processJournalctl()

    val entries= mutableListOf<SyslogRecord>()
    entriesAsPlainString.forEach(){
        val temp=SyslogRecord()
        temp.processString(it)
        entries.add(temp)
    }

    val mapOfEntries=makeMap(entries)
    mapOfEntries.forEach(){ (key,pair)->
        print(key + " : ")
        println(pair)
    }

    println("\nAcum mesajele sunt sortate alfabetic: \n")
    sortMapByMessage(mapOfEntries)

    println("\nFiltrare dupa pid-ul primului entry: \n")
    filterByPID(mapOfEntries,entries[0].PID)
}