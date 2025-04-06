
fun processJournalctl(): List<String>{
    val process=ProcessBuilder("journalctl","--since","30 minutes ago").redirectErrorStream(true).start()
    val outputs=process.inputStream.bufferedReader().readText()
    val list=outputs.split("\n")
    return list.filter{"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)".toRegex().containsMatchIn(it)}
}

//Mar 02 18:56:39 debian gnome-shell[1535]: Created gbm renderer for '/dev/dri/card0'
class SyslogRecord(var Timestamp:String="",var Hostname:String="",var AppName:String="",var PID:String="",var Message:String="") : Comparable<SyslogRecord>{
    fun processString(input:String){
        val tokens=input.split(" ")
        this.Timestamp=tokens[0]+" "+tokens[1]+" "+tokens[2]
        this.Hostname=tokens[3]
        this.AppName=tokens[4].split("[")[0]
        this.PID=tokens[4].split("[")[1].split("]")[0]
        for(i in 5..<tokens.size){
            this.Message=this.Message+tokens[i]+" "
        }
    }

    override fun compareTo(other: SyslogRecord): Int {
        return this.Message.compareTo(other.Message)
    }

    override fun toString():String{
        return "${this.Timestamp} ${this.Hostname} ${this.AppName} [${this.PID}]: ${this.Message}"
    }
}

//fun makeSetOfApps(list: List<SyslogRecord>):Set<String>{
//    val returnSet= mutableSetOf<String>()
//    list.forEach(){
//        returnSet.add(it.AppName)
//    }
//    return returnSet
//}

fun makeMap(listOfEntries:List<SyslogRecord>):Map<String,List<SyslogRecord>>{
    var myMap= mutableMapOf<String,MutableList<SyslogRecord>>()

    listOfEntries.forEach(){
        val currentElem=myMap.getOrPut(it.AppName){ mutableListOf() }
        currentElem.add(it)
        myMap[it.AppName]=currentElem
    }
    return myMap
}

fun sortMapByMessage(myMap:Map<String,List<SyslogRecord>>){
    myMap.forEach(){ (key,entry)->
        val sortedEntry = entry.sorted()
        println(key + " : "+ sortedEntry)
    }
}

fun filterByPID(myMap: Map<String, List<SyslogRecord>>, PID:String){
    myMap.forEach(){ (key,entry) ->
        val temp= mutableListOf<SyslogRecord>()
        entry.forEach(){
            if(it.PID==PID){
                temp.add(it)
            }
        }
        println(key + " : "+ temp)
    }
}