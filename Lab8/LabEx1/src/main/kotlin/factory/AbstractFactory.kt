package factory

import chain.Handler

abstract class AbstractFactory {
    abstract fun getHandler(handler:String): Handler
}