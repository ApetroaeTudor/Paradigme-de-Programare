class Ticket(private val name:String,private val price:Double) {
    override fun toString(): String {
        return "$name: $price"
    }

    fun getPrice():Double{
        return price
    }

    fun identifyByName(name:String):Boolean{
        if(this.name.compareTo(name)==0){
            return true
        }
        return false
    }
}