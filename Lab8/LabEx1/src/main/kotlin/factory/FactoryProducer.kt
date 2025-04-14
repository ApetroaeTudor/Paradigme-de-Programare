package factory

import chain.HappyWorkerHandler

class FactoryProducer {
    fun getFactory(choice:String):AbstractFactory{
        return when(choice){
            "ELITE"->EliteFactory()
            "HAPPY_WORKER"->HappyWorkerFactory()
            else->HappyWorkerFactory()
        }
    }
}