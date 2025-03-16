import kotlin.jvm.Throws

class TicketMaster(private val paymentMethod:PaymentMethod) {
    private val ownedTickets:TicketRepository=TicketRepository()

    fun addTicket(ticketName:String,ticketPrice:Double){
        if(paymentMethod.pay(ticketPrice)){
            ownedTickets.makeAndAddTicket(ticketName,ticketPrice)
        }
    }

    @Throws(Exception::class)
    fun acceptPayment(receivedSum:Double,ticketName:String):Pair<String,Double>{
        try {
            if(ownedTickets.containsTicketByName(ticketName)){
                val returnedPrice:Double=ownedTickets.getTicketPriceByName(ticketName)
                ownedTickets.removeTicketByName(ticketName)
                return Pair(ticketName,returnedPrice)
            }
        }
        catch (e:Exception){
            println(e.message)
        }
        throw Exception("Ticket not found or other unexpected error in acceptPayment")
    }

}