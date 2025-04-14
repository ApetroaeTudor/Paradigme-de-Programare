package chain

interface Handler {
    fun handleRequest(forwardDirection:String, messageToBeProcessed:String)
}