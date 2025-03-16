class User(private val paymentMethod:PaymentMethod) { //dependency injection
    private val ownedTickets:TicketRepository=TicketRepository()

    fun showOwnedTickets(){
        println(ownedTickets)
    }

    fun makePayment(paidAmount:Double):Double{
        if(paymentMethod.pay(paidAmount)){
            return paidAmount
        }
        return 0.0
    }

    fun receiveTicket(ticketData:Pair<String,Double>){
        ownedTickets.makeAndAddTicket(ticketData.first,ticketData.second)
    }


}