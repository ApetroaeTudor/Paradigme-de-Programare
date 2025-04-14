package chain

class HappyWorkerHandler(var next1:Handler?=null, var next2:Handler?=null) :Handler {
    override fun handleRequest(forwardDirection: String, messageToBeProcessed: String) {
        val priority=messageToBeProcessed.split(":")[0]
        val msg=messageToBeProcessed.split(":")[1]
        if(priority=="4"){
            println("Message Processed in HappyWorkerHandler ${msg}")
            if(forwardDirection!="UP"){ //daca e up deja inseamna ca e deja mesaj de confirmare
                next2?.handleRequest("UP","4:MessageHandled")
            }
        }
        else{
            next1?.handleRequest(forwardDirection,messageToBeProcessed)
        }
    }
}