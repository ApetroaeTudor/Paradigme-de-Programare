class Memento(val state:String) {
    fun get_State():String{
        return this.state
    }
}

class Caretaker(){
    val savedStates:MutableList<Memento> = mutableListOf()

    fun addMemento(memento:Memento){
        this.savedStates.add(memento)
    }
    fun get_SavedStates():List<Memento>{
        return this.savedStates
    }

}