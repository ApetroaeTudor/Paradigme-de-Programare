abstract class Observable(){
    val observers:MutableList<Observer> = mutableListOf()

    fun add(observer:Observer){
        this.observers.add(observer)
    }

    fun remove(observer: Observer){
        this.observers.forEach(){
            if(it.getType()==observer.getType()){
                this.observers.remove(it)
            }
        }
    }

    abstract fun notify_All()
}


class Originator:Observable(){
    var message:String=""

    fun setMessage(message:String):Memento{
        val returnVal=saveToMemento()
        this.message=message
        this.notify_All()
        return returnVal
    }


    private fun saveToMemento():Memento{
        val newMemento=Memento(this.message)
        return newMemento
    }




    override fun notify_All() {
        super.observers.forEach(){
            it.update(this.message)
        }
    }

}