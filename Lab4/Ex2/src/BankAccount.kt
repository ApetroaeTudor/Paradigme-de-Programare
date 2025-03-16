class BankAccount(private var availableAmount:Double,
                  private var cardNumber:String,
                  private var expirationDate:Date,
                  private var cvvCode:Int,
                  private var userName:String){

    fun updateAmount(value:Double):Boolean{
        if(availableAmount-value<0){
            println("can't have negative funds!")
            return false
        }
        availableAmount-=value
        return true
    }

}