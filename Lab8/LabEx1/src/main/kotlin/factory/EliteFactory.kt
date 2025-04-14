package factory

import chain.CEOHandler
import chain.ExecutiveHandler
import chain.Handler
import chain.ManagerHandler

class EliteFactory: AbstractFactory() {
    override fun getHandler(handler: String): Handler {
        return when(handler){
            "CEO"->CEOHandler()
            "EXECUTIVE"->ExecutiveHandler()
            "MANAGER"->ManagerHandler()
            else->ManagerHandler()
        }
    }
}