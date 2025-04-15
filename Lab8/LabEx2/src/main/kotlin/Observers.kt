interface Observer{
    fun update(message:String)
    fun getType():String
}

class SmallWordConsumer(val originator: Originator,val caretaker: Caretaker):Observer{
    var counter:Int=0
    override fun update(message:String) {
        if(message.length<=7){
            counter++
            print(" ${message}")
            if(counter==10){
                counter=0
                originator.setMessage(caretaker.get_SavedStates()[caretaker.get_SavedStates().size%10].get_State())
                println("\nRESETTING ON SMALL WORDS")
            }
        }

    }
    override fun getType():String{
        return "SmallWordConsumer"
    }
}

class LargeWordConsumer(val originator: Originator,val caretaker: Caretaker):Observer{
    var counter:Int=0
    override fun update(message:String) {
        if(message.length>7){
            counter++
            print(" ${message}")
            if(counter==7){
                counter=0
                originator.setMessage(caretaker.get_SavedStates()[caretaker.get_SavedStates().size%7].get_State())
                println("\nRESETTING ON LARGE WORDS")
            }
        }

    }
    override fun getType():String{
        return "LargeWordConsumer"
    }
}



