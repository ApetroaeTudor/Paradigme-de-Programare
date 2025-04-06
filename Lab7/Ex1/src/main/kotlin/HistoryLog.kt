import java.io.File
import java.time.LocalDateTime
import kotlin.math.log

fun readFile(path:String):String{
    val myFile= File(path)
    if(!myFile.exists()){
        return ""
    }

    return myFile.readText()
}

fun tokenizeEntries(data:String):List<String>{
    return data.split("\n\n")
}

class HistoryLogRecord(val data:String) : Comparable<HistoryLogRecord>{
    var Timestamp:LocalDateTime= LocalDateTime.of(0,1,1,0,0,0)
    var CommandLine:String=""
    init {

        parseEntry()
    }

    fun parseEntry(){
        val date=this.data.split("Date:")[1].split("\n")[0].trim()

        val year=date.split("-")[0].trim().toInt()
        val month=date.split("-")[1].trim().toInt()
        val day=date.split("-")[2].split("  ")[0].trim().toInt()

        val hour=date.split(":")[0].split("  ")[1].trim().toInt()
        val mins=date.split(":")[1].trim().toInt()
        val secs=date.split(":")[2].split("\n")[0].trim().toInt()

        this.Timestamp=LocalDateTime.of(year,month,day,hour,mins,secs)


        this.CommandLine=this.data.split("Commandline: ")[1].split("\n")[0]

    }

    override fun toString(): String {
        return "Start Date: ${this.Timestamp.year}-${this.Timestamp.month}-${this.Timestamp.dayOfMonth}   ${this.Timestamp.hour}:${this.Timestamp.minute}:${this.Timestamp.second}\n" +
                "CommandLine: ${this.CommandLine}"
    }
    override fun compareTo(other: HistoryLogRecord): Int {
        return this.Timestamp.compareTo(other.Timestamp)
    }

    fun equals(other:HistoryLogRecord):Boolean{
        if(this.CommandLine==other.CommandLine && this.Timestamp.compareTo(other.Timestamp)==0 ){
            return true
        }
        return false
    }
}


fun makeHashMap(logRecords:List<HistoryLogRecord>):MutableMap<LocalDateTime,HistoryLogRecord>{
    val returnval= mutableMapOf<LocalDateTime,HistoryLogRecord>()

    logRecords.forEach(){
        returnval.put(it.Timestamp,it)
    }

    return returnval
}

fun <K> replaceInMap(target:HistoryLogRecord, replacement:HistoryLogRecord, obj:MutableMap<K,*>){
    val myMap=obj as MutableMap<K,HistoryLogRecord>
    myMap.forEach(){ (key,value)->
        if(value.equals(target)){
            myMap[key]=replacement
        }
    }

    myMap.forEach(){ (key,value)->
        print(key)
        println(" <---> $value")
    }
}


