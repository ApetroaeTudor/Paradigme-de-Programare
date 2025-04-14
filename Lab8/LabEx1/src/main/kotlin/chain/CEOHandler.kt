package chain

class CEOHandler(var next1:Handler?=null,var next2:Handler?=null) : Handler {
    override fun handleRequest(forwardDirection: String, messageToBeProcessed: String) {
        val priority=messageToBeProcessed.split(":")[0]
        val msg=messageToBeProcessed.split(":")[1]
        if(priority=="1"){
            println("Message Processed in CEOHandler ${msg}")
            if(forwardDirection!="UP"){ //daca e up deja inseamna ca e deja mesaj de confirmare
                next2?.handleRequest("UP","1:MessageHandled")
            }
        }
        else{
            next1?.handleRequest(forwardDirection,messageToBeProcessed)
        }
    }
}