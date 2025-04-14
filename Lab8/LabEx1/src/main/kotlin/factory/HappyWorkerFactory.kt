package factory

import chain.CEOHandler
import chain.Handler
import chain.HappyWorkerHandler

class HappyWorkerFactory:AbstractFactory() {
    override fun getHandler(handler: String): Handler {
        return HappyWorkerHandler()
    }
}