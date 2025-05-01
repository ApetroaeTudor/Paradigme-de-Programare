package lab.pp

interface AbstractFactory{
    fun getHandler(handler:String) : Handler
}

class EliteFactory() : AbstractFactory{
    override fun getHandler(handler: String): Handler {
        when(handler.lowercase()){
            "ceo" -> return CEOHandler()
            "executive" -> return ExecutiveHandler()
            "manager" -> return ManagerHandler()
            else -> throw Exception("Invalid type given to concrete factory\n")
        }
    }
}

class HappyWorkerFactory() : AbstractFactory{
    override fun getHandler(handler: String): Handler {
        when(handler.lowercase()){
            "happyworker"-> return HappyWorkerHandler()
            else -> throw Exception("Invalid type given to concrete factory\n")
        }
    }
}



abstract class FactoryProducer private constructor(){
    companion object {
        fun getFactory(choice: String): AbstractFactory{
            when(choice.lowercase()){
                "elite"-> return EliteFactory()
                "happyworker"-> return HappyWorkerFactory()
                else -> throw Exception("Invalid type given to abstract factory\n")
            }
        }
    }
}