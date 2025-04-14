import chain.CEOHandler
import chain.ExecutiveHandler
import chain.HappyWorkerHandler
import chain.ManagerHandler
import factory.EliteFactory
import factory.FactoryProducer
import factory.HappyWorkerFactory

fun main() {
    val myFactoryProducer = FactoryProducer()
    val myEliteFactory = myFactoryProducer.getFactory("ELITE")
    val myHappyWorkerFactory = myFactoryProducer.getFactory("HAPPY_WORKER")

    var myCEOHandler1 = myEliteFactory.getHandler("CEO") as CEOHandler
    var myCEOHandler2 = myEliteFactory.getHandler("CEO") as CEOHandler

    var myExecutiveHandler1 = myEliteFactory.getHandler("EXECUTIVE") as ExecutiveHandler
    var myExecutiveHandler2 = myEliteFactory.getHandler("EXECUTIVE") as ExecutiveHandler

    var myManagerHandler1 = myEliteFactory.getHandler("MANAGER") as ManagerHandler
    var myManagerHandler2 = myEliteFactory.getHandler("MANAGER") as ManagerHandler

    var myHappyWorkerHandler1 = myHappyWorkerFactory.getHandler("WORKER") as HappyWorkerHandler
    var myHappyWorkerHandler2 = myHappyWorkerFactory.getHandler("WORKER") as HappyWorkerHandler

    myCEOHandler1.next1=myExecutiveHandler1; myExecutiveHandler1.next1=myManagerHandler1; myManagerHandler1.next1=myHappyWorkerHandler1; myHappyWorkerHandler1.next1=myHappyWorkerHandler2
    myCEOHandler2.next1=myExecutiveHandler2; myExecutiveHandler2.next1=myManagerHandler2; myManagerHandler2.next1=myHappyWorkerHandler2;
    myCEOHandler1.next2=myCEOHandler2
    myCEOHandler2.next2=myCEOHandler1

    myExecutiveHandler2.next2=myExecutiveHandler1
    myManagerHandler2.next2=myManagerHandler1
    myHappyWorkerHandler2.next2=myHappyWorkerHandler1

    val msg1 = "1:Greetings"
    val msg2 = "2:Hello"
    val msg3 = "3:Hey"
    val msg4 = "4:Hi"

    myCEOHandler2.handleRequest("right",msg1)
    println()

    myCEOHandler2.handleRequest("right",msg4)


}