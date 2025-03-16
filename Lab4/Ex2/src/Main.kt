fun main() {
    val expirationDate:Date=Date(2027,5,21)
    val myBankAccount:BankAccount=BankAccount(1500.0,"312312",expirationDate,231,"UserName")
    val myUser:User=User(CardPayment(myBankAccount))

    val TMBankAccount:BankAccount=BankAccount(10000.0,"312312321",expirationDate,321,"TicketMaster")

    val ticketMaster:TicketMaster=TicketMaster(CardPayment(TMBankAccount))
    ticketMaster.addTicket("Show1",120.0)
    ticketMaster.addTicket("Show2",500.0)
    ticketMaster.addTicket("Show3",400.0)
    ticketMaster.addTicket("Show3",400.0)
    ticketMaster.addTicket("Show4",1200.0)


    try{
        myUser.receiveTicket(ticketMaster.acceptPayment(myUser.makePayment(450.0),"Show2"))
    }
    catch (e:Exception){
        println(e.message)
    }

    try{
        myUser.receiveTicket(ticketMaster.acceptPayment(myUser.makePayment(400.0),"Show1"))
    }
    catch (e:Exception){
        println(e.message)
    }

    myUser.showOwnedTickets()

}