class CardPayment(private val bankAccount: BankAccount) : PaymentMethod {
    override fun pay(fee: Double): Boolean {
        return bankAccount.updateAmount(fee)
    }
}

class CashPayment(private var availableAmount:Double) : PaymentMethod {
    override fun pay(fee: Double): Boolean {
        if(availableAmount-fee<0){
            println("can't have negative funds!")
            return false
        }
        availableAmount-=fee
        return true
    }
}

