class Date(private val year:Int,private val month:Int,private val day:Int) {
    override fun toString(): String {
        return "$year.$month.$day"
    }
}