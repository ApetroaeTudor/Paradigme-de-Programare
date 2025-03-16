class Date(private var year:Int,private var month:Int, private var day:Int) {
    override fun toString(): String {
        return "$year,$month,$day"
    }
}