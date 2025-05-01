package lab.pp
import kotlinx.coroutines.*
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import java.util.LinkedList
import java.util.concurrent.SynchronousQueue

val myMutex = Mutex()
val myContext = newSingleThreadContext("myCtx")

fun getHandlerType(handler:Handler) : String{
    when(handler){
        is CEOHandler-> return "CEOHandler"
        is ExecutiveHandler -> return "ExecutiveHandler"
        is ManagerHandler -> return "ManagerHandler"
        is HappyWorkerHandler -> return "HappyWorkerHandler"
        else -> throw Exception("\nUnknown handler type\n")
    }
}


interface Handler{
    abstract var next1:Handler?
    abstract var next2:Handler?
    abstract val priority:Int
    suspend fun handleRequest(messageToBeProcessed:Message){
        val selfRef = this
        val msgPriority =messageToBeProcessed.getPriority()
        val msgType = messageToBeProcessed.getType()
        when(msgType){
            "request"->{
                if(msgPriority == priority){
                               CoroutineScope(myContext).launch {
                                   delay(500)
                                   println("Chain changed on handler ${getHandlerType(selfRef)}")
                                    myMutex.withLock {
                                        next2?.handleRequest(Response(messageToBeProcessed.primitiveFormat))
                                    }
                                }
                }
                else{
                        next1?.let{
                            CoroutineScope(myContext).launch {
                                delay(500)
                                println("Message sent on the same chain on handler ${getHandlerType(selfRef)}")
                                myMutex.withLock {
                                    next1?.handleRequest(messageToBeProcessed)
                                }
                            }

                        } ?: run {
                            CoroutineScope(myContext).launch {
                                delay(500)
                                println("Message can't be processed\n")
                            }
                        }

                }
            }
            "response"->{
                when(messageToBeProcessed.nrOfMovesDone){
                    0->{
                                    CoroutineScope(myContext).launch {
                                        delay(500)
                                        println("Response sent on the same chain, from ${getHandlerType(selfRef)}")
                                        myMutex.withLock {
                                            messageToBeProcessed.nrOfMovesDone++
                                            next1?.handleRequest(messageToBeProcessed)
                                        }
                        }

                    }
                    1->{
                                    CoroutineScope(myContext).launch {
                                        delay(500)
                                        println("Response sent back to the upper chain, from ${getHandlerType(selfRef)}")
                                        myMutex.withLock {
                                            messageToBeProcessed.nrOfMovesDone++
                                            next2?.handleRequest(messageToBeProcessed)
                                        }
                        }

                    }
                    2->{
                        CoroutineScope(myContext).launch {
                            delay(500)
                            myMutex.withLock {
                                println(messageToBeProcessed.getContent()+"\n")
                                println("Final processing was done on ${getHandlerType(selfRef)}")
                            }
                        }

                    }
                }

            }
        }
    }
}

class CEOHandler(override var next1:Handler?=null, override var next2:Handler?=null) : Handler{
    override val priority = 1;

}

class ExecutiveHandler(override var next1: Handler?=null,override var next2: Handler?=null) : Handler{
    override val priority = 2;

}

class ManagerHandler(override var next1: Handler?=null,override var next2: Handler?=null) : Handler{
    override val priority = 3;

}

class HappyWorkerHandler(override var next1: Handler?=null,override var next2: Handler?=null) : Handler{
    override val priority = 4;

}