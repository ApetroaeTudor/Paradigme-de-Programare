class TicketRepository() {
    private val tickets:MutableList<Ticket> = mutableListOf()


    fun makeAndAddTicket(name:String,price:Double){
        tickets.add(Ticket(name,price))
    }

    fun getTicketPriceByName(name:String):Double{
        tickets.forEach(){
            if(it.identifyByName(name)){
                return it.getPrice()
            }
        }
        throw Exception("Did not find ticket")
    }

    fun removeTicketByName(name:String){
        tickets.removeIf{it.identifyByName(name)}
    }

    fun containsTicketByName(name:String):Boolean{
        tickets.forEach(){
            if(it.identifyByName(name)){
                return true
            }
        }
        return false
    }

    override fun toString(): String {
        return tickets.toString()
    }


}