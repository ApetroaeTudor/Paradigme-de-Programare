
abstract class LogicGate{
    abstract val logicCalculator:LogicCalculator
    abstract fun getOutput():Boolean
}

interface LogicCalculator{
    fun calculateLogicFunction():Boolean
}

class ANDFSM()


class ANDLogicCalculator(val inputs:MutableList<Boolean>):LogicCalculator{
    enum class State{
        START,TRUE,FALSE
    }
    override fun calculateLogicFunction(): Boolean {
        var state=State.START

        inputs.forEach(){
            state=when(state){
                State.START,State.TRUE->
                    if(it==false){
                        State.FALSE
                    }
                    else{
                        State.TRUE
                    }
                State.FALSE->State.FALSE

            }
        }

        return when(state){
            State.TRUE->true
            State.FALSE->false
            State.START->false
        }
    }
}

class ANDGate private constructor(override val logicCalculator: LogicCalculator) : LogicGate(){
    val inputList:List<Boolean> = mutableListOf()

    companion object{
        fun build() = Builder()
    }

    override fun getOutput(): Boolean {
        return logicCalculator.calculateLogicFunction()
    }


    class Builder{
        val inputList:MutableList<Boolean> = mutableListOf()
        fun addInput(input:Boolean):Builder{
            this.inputList.add(input)
            return this
        }
        fun build():ANDGate{
            val calculator=ANDLogicCalculator(inputList)
            return ANDGate(calculator)
        }


    }


}

fun main() {
    val myANDGate=ANDGate.build()
        .addInput(true)
        .addInput(true)
        .addInput(false)
        .build()
    println(myANDGate.getOutput())
}