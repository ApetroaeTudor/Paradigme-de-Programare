package lab.pp

import kotlinx.coroutines.*

fun main() = runBlocking{
    val msgString1 = "1.HelloCeo"
    val msgString2 = "3.HelloManager"
    val msgString3 = "6.HelloInvalid"
    val msgString4 = "4.HelloHappyWorker"

    val msg1 = Request(msgString1)
    val msg2 = Request(msgString2)
    val msg3 = Request(msgString3)
    val msg4 = Request(msgString4)

    val myEliteFactory = FactoryProducer.getFactory("elite")
    val myHappyWorkerFactory = FactoryProducer.getFactory("HappyWorker")

    val CEO1 = myEliteFactory.getHandler("ceo")
    val CEO2 = myEliteFactory.getHandler("ceo")

    val executive1 = myEliteFactory.getHandler("executive")
    val executive2 = myEliteFactory.getHandler("executive")

    val manager1 = myEliteFactory.getHandler("manager")
    val manager2 = myEliteFactory.getHandler("manager")

    val happyWorker1 = myHappyWorkerFactory.getHandler("happyWorker")
    val happyWorker2 = myHappyWorkerFactory.getHandler("happyWorker")

    CEO1.next1 = executive1; CEO1.next2 = CEO2
    executive1.next1 = manager1; executive1.next2 = executive2
    manager1.next1 = happyWorker1; manager1.next2 = manager2
    happyWorker1.next1 = null; happyWorker1.next2 = happyWorker2

    CEO2.next1 = CEO2; CEO2.next2 = CEO1
    executive2.next1 = CEO2; executive2.next2 = executive1
    manager2.next1 = executive2; manager2.next2 = manager1
    happyWorker2.next1 = manager2; happyWorker2.next2 = happyWorker1

    val job1 = async {
        try{
            CEO1.handleRequest(msg4)
        }
        catch (e:Exception){
            println(e.message)
        }
    }

    job1.await()
    delay(5000)
    if(job1.isCompleted){
        println("\nMessage Processing done\n")
    }

}



